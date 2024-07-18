# trial_b.py
import RPi.GPIO as gpio
import time
import cv2
import threading

# Pin setup
TRIGER = 24
ECHO = 23
LED = 18
SWITCH = 25

# Distance thresholds
MIN_DIST = 10
MAX_DIST = 30
TIME_THRESHOLD = 5  # 5 seconds

# Initialize time tracking variables
startTime = time.time()
in_range_start_time = None  # Time when the object first detected in range
led_on = False  # LED state

# Shared variable for storing distance measurement
distance_measurements = {"dist1": 0, "dist2": 0}

def setup():
    print("Setting up GPIO...")
    gpio.setmode(gpio.BCM)
    gpio.setup(TRIGER, gpio.OUT)
    gpio.setup(ECHO, gpio.IN)
    gpio.setup(LED, gpio.OUT)
    gpio.setup(SWITCH, gpio.IN, pull_up_down=gpio.PUD_UP)
    print("GPIO setup complete.")

def measure_distance():
    global startTime  # Declare global to modify the variable
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

    # Update shared variable
    distance_measurements["dist1"] = dist1
    distance_measurements["dist2"] = dist2

    return dist1, dist2

def check_switch():
    state = gpio.input(SWITCH)
    print(f"Switch state: {state}")
    return state == gpio.LOW

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

def main():
    global led_on, in_range_start_time
    try:
        setup()
        while True:
            if check_switch():  # 스위치가 눌렸을 때
                print("Switch pressed, turning off LED.")
                gpio.output(LED, gpio.LOW)
                led_on = False
                in_range_start_time = None
                time.sleep(1)  # 스위치 입력 안정화

            dist1, dist2 = measure_distance()
            print("Dist1", dist1, "cm", ", Dist2", dist2, "cm")

            if MIN_DIST <= dist1 <= MAX_DIST:
                if in_range_start_time is None:
                    in_range_start_time = time.time()
                elif time.time() - in_range_start_time >= TIME_THRESHOLD:
                    print("Object detected within range for threshold time, turning on LED and capturing image.")
                    gpio.output(LED, gpio.HIGH)
                    led_on = True
                    capture_image()  # Capture image when LED turns on
            else:
                in_range_start_time = None
                if not led_on:
                    gpio.output(LED, gpio.LOW)

    except KeyboardInterrupt:
        gpio.cleanup()
        print("Cleanup and exit.")

def start_sensor():
    thread = threading.Thread(target=main)
    thread.start()

if __name__ == "__main__":
    main()
