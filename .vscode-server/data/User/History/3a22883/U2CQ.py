import picamera2
from time import sleep

# Picamera2 초기화
camera = Picamera2()

def capture_image(image_path):
    camera.start_preview()
    sleep(2)  # 카메라 준비 시간
    camera.capture_file(image_path)
    camera.stop_preview()

capture_image('./catpure.png')