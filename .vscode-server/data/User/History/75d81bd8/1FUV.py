from flask import Flask, render_template, Response
import cv2
import RPi.GPIO as gpio
import time
import threading

app = Flask(__name__)

# 핀 설정
TRIGER = 24
ECHO = 23
LED = 18
SWITCH = 25  # 스위치 핀 설정

gpio.setmode(gpio.BCM)
gpio.setup(TRIGER, gpio.OUT)
gpio.setup(ECHO, gpio.IN)
gpio.setup(LED, gpio.OUT)
gpio.setup(SWITCH, gpio.IN, pull_up_down=gpio.PUD_UP)  # 스위치 핀 풀업 설정

# 거리 임계값
MIN_DIST = 10
MAX_DIST = 30
TIME_THRESHOLD = 5  # 5 seconds

# 시간 추적 변수 초기화
startTime = time.time()
in_range_start_time = None  # 물체가 범위 내에 처음 감지된 시간
led_on = False  # LED 상태

# 카메라 초기화
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def sensor_led_control():
    global in_range_start_time, led_on
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
                    gpio.output(LED, gpio.HIGH)
                    if not led_on:  # LED가 켜진 적이 없다면 사진 촬영
                        ret, frame = cap.read()
                        if ret:
                            cv2.imwrite('/home/pi/image.jpg', frame)
                            print("사진이 성공적으로 촬영되었습니다!")
                        else:
                            print("프레임을 캡처하는 데 실패했습니다.")
                        led_on = True
            else:
                in_range_start_time = None
                if not led_on:
                    gpio.output(LED, gpio.LOW)
    except KeyboardInterrupt:
        gpio.cleanup()
        cap.release()
        cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=sensor_led_control)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=5000)
