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
    if not cap.isOpened():
        print("Failed to open camera.")
        return
    
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image from camera.")
        cap.release()
        return

    try:
        image_path = os.path.join(app.root_path, 'static', 'captured_image.jpg')
        cv2.imwrite(image_path, frame)
        print(f"Image captured and saved to {image_path}.")
    except Exception as e:
        print(f"Failed to save image: {e}")

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
    photo = 'captured_image.jpg' if os.path.exists(os.path.join(app.root_path, 'static', 'captured_image.jpg')) else None
    return render_template('index.html', photo=photo)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

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
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
