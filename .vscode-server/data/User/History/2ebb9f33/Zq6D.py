import RPi.GPIO as GPIO
import time

# 초음파 센서 핀 번호 설정
TRIG_PIN = 18
ECHO_PIN = 24

# LED(다이오드) 핀 번호 설정
LED_PIN = 17

# 초음파 센서 초기화
def setup_ultrasonic_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(LED_PIN, GPIO.OUT)

# 초음파 센서를 이용해 거리 측정
def measure_distance():
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)
    
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
        
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance

# 메인 함수
def main():
    setup_ultrasonic_sensor()
    
    try:
        while True:
            distance = measure_distance()
            
            # 만약 택배가 놓여진 상태라면
            if distance < 5:  # 여기서 5는 센서에서 측정된 거리에 따라 조정할 수 있습니다.
                time.sleep(10)  # 택배가 멈춘 상태로 간주할 시간 (여기서는 10초)
                if measure_distance() < 5:
                    GPIO.output(LED_PIN, GPIO.HIGH)  # LED(다이오드) 켜기
                else:
                    GPIO.output(LED_PIN, GPIO.LOW)  # LED(다이오드) 끄기
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
