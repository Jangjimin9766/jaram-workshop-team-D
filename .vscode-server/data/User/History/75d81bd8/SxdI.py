# app.py
from flask import Flask, render_template, Response, jsonify
import cv2
import os
import trial_b  # Ensure trial_b.py is in the same directory as app.py
import time
import threading

app = Flask(__name__)

def capture_image():
    print("Capturing image...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured.")
    else:
        print("Failed to capture image.")
    cap.release()

def monitor_led():
    while True:
        if trial_b.led_status["on"]:
            print("LED is on, capturing image.")
            capture_image()
            trial_b.led_status["on"] = False  # Reset the status after capturing the image
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/captured_image')
def captured_image():
    if os.path.exists('captured_image.jpg'):
        return Response(open('captured_image.jpg', 'rb').read(), mimetype='image/jpeg')
    else:
        return "No image captured", 404

@app.route('/distance')
def distance():
    return jsonify(trial_b.distance_measurements)

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == '__main__':
    trial_b.start_sensor()  # Start the sensor in a separate thread
    monitor_thread = threading.Thread(target=monitor_led)
    monitor_thread.start()
    app.run(debug=True, use_reloader=False)
