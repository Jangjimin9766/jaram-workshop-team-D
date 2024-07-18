import RPi.GPIO as gpio
import time
import cv2
import threading
from flask import Flask, render_template_string, Response

# GPIO 핀 설정
TRIGER = 24
ECHO = 23
LED = 18
SWITCH = 25  # 스위치 핀 설정

# GPIO 초기화
gpio.setmode(gpio.BCM)
gpio.setup(TRIGER, gpio.OUT)
gpio.setup(ECHO, gpio.IN)
gpio.setup(LED, gpio.OUT)
gpio.setup(SWITCH, gpio.IN, pull_up_down=gpio.PUD_UP)  # 스위치 핀 풀업 설정

# 거리 및 시간 임계값 설정
MIN_DIST = 10
MAX_DIST = 30
TIME_THRESHOLD = 5  # 5 seconds

# 초기화 변수
startTime = time.time()
in_range_start_time = None  # Time when the object first detected in range
led_on = False  # LED state
last_photo_time = 0  # 마지막으로 사진을 찍은 시간

# Flask 웹 서버 설정
app = Flask(__name__)
photo_path = '/home/jaram/photos/'  # 사진 저장 경로

# 웹 페이지 템플릿
html_template = """
<!doctype html>
<html>
    <head>
        <title>택배 알리미</title>
    </head>
    <body>
        <h1>택배 알리미</h1>
        {% if photo %}
            <img src="{{ url_for('static', filename='photo.jpg') }}" alt="택배 사진">
        {% else %}
            <p>택배가 감지되지 않았습니다.</p>
        {% endif %}
        <img src="{{ url_for('video_feed') }}" alt="라이브 카메라">
    </body>
</html>
"""

@app.route('/')
def index():
    photo = 'photo.jpg' if led_on else None
    return render_template_string(html_template, photo=photo)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

def take_photo():
    global last_photo_time
    current_time = time.time()
    if current_time - last_photo_time >= TIME_THRESHOLD:
        # 카메라 객체 생성
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
            return

        ret, frame = cap.read()
        if ret:
            cv2.imwrite(photo_path + 'photo.jpg', frame)
            print("사진이 저장되었습니다.")
            last_photo_time = current_time  # 사진을 찍은 시간 업데이트

        cap.release()

def generate_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 프레임을 JPEG 형식으로 인코딩하여 바이트 데이터로 변환
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def sensor_loop():
    global led_on, in_range_start_time
    try:
        while True:
            if gpio.input(SWITCH) == gpio.LOW:  # 스위치가 눌렸을 때
                gpio.output(LED, gpio.LOW)
                led_on = False
                in_range_start_time = None
                time.sleep(1)  # 스위치 입력 안정화

            gpio.output(TRIGER, gpio.LOW)
            time.sleep(0.1)
            gpio.output(TRIGER, gpio.HIGH)
            time.sleep(0.00002)
            gpio.output(TRIGER, gpio.LOW)

            while gpio.input(ECHO) == gpio.LOW:
                startTime = time.time()  # 1sec unit

            while gpio.input(ECHO) == gpio.HIGH:
                endTime = time.time()

            period = endTime - startTime
            dist1 = round(period * 1000000 / 58, 2)
            dist2 = round(period * 17241, 2)

            print("Dist1", dist1, "cm", ", Dist2", dist2, "cm")

            if MIN_DIST <= dist1 <= MAX_DIST:
                if in_range_start_time is None:
                    in_range_start_time = time.time()
                elif time.time() - in_range_start_time >= TIME_THRESHOLD:
                    gpio.output(LED
