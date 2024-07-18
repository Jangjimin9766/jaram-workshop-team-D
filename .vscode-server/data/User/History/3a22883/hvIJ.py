from picamera import PiCamera

camera = PiCamera()

def capture_image(image_path):
    camera.start_preview()
    time.sleep(2)  # 카메라 준비 시간
    camera.capture(image_path)
    camera.stop_preview()
