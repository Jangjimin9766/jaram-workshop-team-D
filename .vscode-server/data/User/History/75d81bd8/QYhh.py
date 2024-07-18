# app.py
from flask import Flask, render_template, Response
import cv2
import os
import trial_b

app = Flask(__name__)

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
    trial_b.setup()  # Ensure GPIO setup is done before starting Flask
    app.run(debug=True, use_reloader=False)
