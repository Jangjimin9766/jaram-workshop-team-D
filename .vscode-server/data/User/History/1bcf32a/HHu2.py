import threading

# 거리 측정 및 LED 제어
def detect_package():
    while True:
        distance = measure_distance()
        print(f"Measured Distance: {distance} cm")
        if distance < 20:  # 예: 20cm 이내에 물체가 있으면
            led_on()
            capture_image('/home/pi/captured_image.jpg')
        else:
            led_off()
        time.sleep(1)

# 백그라운드에서 실행할 스레드 시작
threading.Thread(target=detect_package).start()

# 웹 서버 실행
app.run(host='0.0.0.0', port=5000)
