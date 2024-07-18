import picamera as pic
from time import sleep

camera = pic.PiCamera()
camera.brightness = 58
camera.sharpness = 10
camera.contrast = 10

camera.start_preview()
sleep(5)
camera.capture('image.png')
camera.stop_preview()

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()