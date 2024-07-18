sudo apt update
ifconfig -a
sudo apt update
sudo apt upgrade
date
clear
raspi-config .
sudo raspi-config
df -h
clear
inti 0
init 0
sudo raspi-config
/bin/python /home/jaram/projects/trial_b.py
sudo apt-get update
sudo apt-get install python3-rpi.gpio
sudo apt-get install python3-picamera
sudo apt-get install python3-flask
sudo apt-get update
sudo apt-get install python3-rpi.gpio python3-picamera python3-flask
sudo raspi-config
sudo apt get install python3 picamera
sudo apt -get install python3 -picamera
sudo apt- get install pytho3- picamera
sudo raspi-config
sudo apt update
/bin/python /home/jaram/projects/trial_b.py
sudo apt- get install python- picamera
sudo apt- get install python3- picamera
sudo apt-get install python3-picamera
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install picamera
sudo apt update
sudo apt upgrade
sudo apt install libcamera-apps libcamera-dev
sudo apt install python3-pip
pip3 install picamera2
python3 -m venv ~/myenv
source ~/myenv/bin/activate
pip install picamera2
deactivate
sudo apt-get update
sudo apt-get install libcap-dev
python3 -m venv ~/myenv
source ~/myenv/bin/activate
pip install picamera2
deactivate
clear
pip3 install picamera2
clear
ls /dev/video*
cat /dev/video10
cat /dev/video11
cat /dev/video12
clear
v4l2-ctl 
v4l2-ctl  --list-devices
c.ear
clear
python3 testjimin/camera.py 
pip3 install libcamera
import RPi.GPIO as GPIO
import time
import threading
from flask import Flask, send_file
from picamera2 import Picamera2
from time import sleep
# GPIO 핀 설정
TRIG_PIN = 23
ECHO_PIN = 24
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
app = Flask(__name__)
camera = Picamera2()
# 거리 측정 함수
def measure_distance():
# LED 제어 함수
def led_on():
def led_off():
# 카메라 이미지 캡처 함수
def capture_image(image_path):
# 웹 서버 설정
@app.route('/image')
def get_image():
# 백그라운드에서 실행할 스레드 시작
threading.Thread(target=detect_package, daemon=True).start()
# 웹 서버 실행
if __name__ == '__main__':;     app.run(host='0.0.0.0', port=5000)
sudo raspi-config
/home/jaram/myenv/bin/python /home/jaram/testjimin/inter.py
python3 -m venv ~/myenv
source ~/myenv/bin/activate
/home/jaram/myenv/bin/python /home/jaram/testjimin/camera.py
/bin/python /home/jaram/.vscode-server/extensions/ms-python.python-2024.10.0-linux-arm64/python_files/printEnvVariablesToFile.py /home/jaram/.vscode-server/extensions/ms-python.python-2024.10.0-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo raspi-config
sudo apt update
sudo apt upgrade
sudo apt install libcamera-apps
sudo nano /boot/config.txt
sudo nano /boot/firmware/conftxt
sudo nano /boot/firmware/config.txt
sudo reboot
raspistill -o test.jpg
sudo apt-get upgrade
sudo apt-get install python-picamera
sudo rpi-update
/bin/python /home/jaram/.vscode-server/extensions/ms-python.python-2024.10.0-linux-arm64/python_files/printEnvVariablesToFile.py /home/jaram/.vscode-server/extensions/ms-python.python-2024.10.0-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo rpi-update
/home/jaram/myenv/bin/python /home/jaram/projects/trial_a.py
libcamera-hello
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
sudo raspi-config
sudo apt update
sudo apt full-upgrade
sudo rpi-update
sudo reboot
vcgencmd get_camera
sudo apt install libcamera-apps
sudo apt update
sudo apt full-upgrade
sudo rpi-update
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
sudo raspi-config
sudo reboot
libcamera-hello
lsmod | grep bcm2835_v412
sudo modprobe bcm2835-v4l2
vcgencmd get_camera
sudo apt install --reinstall libcamera-apps
sudo raspi-config
sudo reboot
libcamera-hello
dmesg | grep -i camera
libcamera-hello
sudo libcamera-hello
vcgencmd get_camera
clear
ls
python3 ./testjimin/camera.py 
pip3 install picamera2
clear
sudo apt install python3-virtualenv
clear
ls
virtualenv iot
source ./iot/bin/activate
clear
ls
pip3 install picamera2
clear
python3 ./testjimin/camera.py 
pip3 install libcamera
sudo apt search libcamera
sudo apt install libcamera
sudo apt install libcamera0
python3 ./testjimin/camera.py 
clear
pip3 install pylibcamera
pip3 install libcamera
exit
clear
python3 ./testjimin/camera.py 
sudo apt install picamer2
sudo apt install python3-pycamera2
sudo apt install python3-pycamera
sudo apt search pycamera | grep python3
sudo apt search libcamera | grep python3
sudo apt install python3-picamera2
clear
ls
python3 ./testjimin/camera.py 
clear
python3 ./testjimin/camera.py 
clear
python3 ./testjimin/py
python3 ./testjimin/camera.py 
sudo python3 ./testjimin/camera.py 
clear
python3 testjimin/camera.py 
clear
libcamera
libcamera-hello
clear
ls
clear
ls
clear
ls
sudo apt install libcamera
sudo apt install libcamera0
clear
libcamera
libcamera-hello
clear
libcamera-hello
clear
python3 ./testjimin/camera.py 
clear
exit
sudo pip3 install RPi.GPIO
/bin/python /home/jaram/.vscode-server/extensions/ms-python.python-2024.10.0-linux-arm64/python_files/printEnvVariablesToFile.py /home/jaram/.vscode-server/extensions/ms-python.python-2024.10.0-linux-arm64/python_files/deactivate/bash/envVars.txt
clear
python3 ./testjimin/camera.py 
sudo apt install python3-pycamera2
sudo apt install python3-pycamer
sudo apt install python3-pycamera2
sudo apt search 
sudo apt install python3-picamera2
python3 ./testjimin/camera.py 
rpicam
sudo apt install rpicam
sudo apt search rpicam
sudo apt install rpicam-apps-light
sudo apt install rpicam-apps-lte
sudo apt install rpicam-apps-lite
rpicam-hello 
rpicam-raw -h
rpicam-raw --list-cameras
clear
sudo apt install libcamer0
sudo apt install libcamera0
clear
ls
clear
libcamera
clear
sudo apt seasrch libcamera
sudo apt search libcamera
sudo apt seasrch libcamera-tools
sudo apt install libcamera-tools
clear
libcamerify 
clear
libcamerify -h
libcamerify python3 ./testjimin/camera.py 
clear
cam 
cam  -I
cam  --info
cam -L
cam -l
clear
cam -l
clear
sudo raspi-config
clear
v4l2-ctl --list-formats
clear
sudo apt search tcamproperty
sudo apt isntall tcam-property
sduo apt install tcam-property
sudoapt install tcam-property
sudo apt install tcam-property
sudo apt install tiscamera
ifconfig -a
libcamera-hello
dmesg | grep -i camera
sudo raspi-config
vcgencmd get_camera
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
sudo modprobe bcm2835-v4l2
sudo apt update
sudo apt install --reinstall libcamera-apps
sudo reboot
sudo raspi-config
dmesg | grep -i camera
libcamera-hello
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
libcamera-hello
sudo modprobe bcm2835-v4l2
sudo apt install --reinstall libcamera-apps
vcgencmd get_camera
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
vcgencmd get_camera
/bin/python /home/jaram/projects/trial_b.py
/bin/python /home/jaram/projects/trial_a.py
/bin/python /home/jaram/projects/trial_b.py
ls
eixt
exit
/bin/python /home/jaram/projects/trial_b.py
sudo apt- get update
sudo apt get update
sudo apt update
sudo apt install python-picamera
sudo apt install python3-picamera
sudo apt install python3-picamera0
sudo apt install python3-picamera
sudo apt install python3-pip
pip3 install picamera
sudo apt install python3-picamera
sudo apt install python3-picamera0
sudo raspi-config
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
libcamera-hello
sudo nano /boot/cmdline.txt
sudo nano /boot/firmware/cmdline.txt
sudo apt install python3-picamera
sudo apt install python3-picamera0
sudo rpi-update
sudo raspi-confi
sudo raspi-config
ls
find . -name output.mp4
cd test
ls
clear
ls
ls -lah
ls
ls -lha
clear
ls
ls -lah
exit
libcamera-hello --qt-preview
sudo apt update
sudo apt install qt5-default qtwayland5
sudo apt install qt5-qmake libqt5gui5 libqt5core5a libqt5widgets5 libcamera0 libcamera-tools
sudo apt --fix-broken install
sudo apt clean
sudo apt update
sudo apt upgrade
sudo dpkg --configure -a
sudo apt-get autoremove
sudo apt install libcamera-apps
sudo apt-get install -t buster-backports libcamera-dev libcamera-tools
sudo nano /etc/apt/sources.list
sudo apt update
lsb_release -a
sudo nano /etc/apt/sources.list
clear
ls
python3 -c "import picamera"
source iot/bin/activate
python3 -c "import picamera"
clear
unaem -a
uname -a
clear
sudo apt install python3-picamera
pip3 install picamera
clear
ls
python3 -c 'import picamera'
pip3 install opencv
pip3 install py-opencv
pip3 install python-opencv
pip3 install opencv-python
sudo raspi-config
clear
ls
mkdir test
cd test
ls
clear
ls
python3
clear
python3
clear
ls
pwd
clear
ls
rm vid.raw 
ls
clear
ls
lss
s
clear
ls
python3
clear
ls
vi test.py
clear
ls
clear
ls
rm test.py 
vi test.py
python3 test.py 
ls
rm your_video.avi 
ls
clear
ls
vi test.py 
exit
clear
ls
clear
ls
exit
/bin/python /home/jaram/test/test.py
pip3 install opencv-python
python3 /home/jaram/test/test.py
python3 -m venv ~/myenv
source ~/myenv/bin/activate
pip install opencv-python
python /home/jaram/test/test.py
/bin/python /home/jaram/test/test.py
pip install opencv-python3
pip install opencv-python
python /home/jaram/test/test.py
source ~/myenv/bin/activate
pip list
clear
deactivate
pip install opencv-python
pip install opencv-python3-xyz
sudo apt install python3-xyz
/bin/python /home/jaram/test/test.py
python -m venv cv_env
pip install opencv-python
/home/jaram/cv_env/bin/python /home/jaram/cv_env/test.py
pip install flask
python app.py
cd /home/jaram
nano app.py
mkdir -p /home/jaram/templates
nano /home/jaram/templates/index.html
python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/projects/trial_b.py
source /home/jaram/cv_env/bin/activate
pip install RPi.GPIO
python /home/jaram/projects/trial_b.py
/home/jaram/cv_env/bin/python /home/jaram/projects/trial_b.py
ls /dev/video*
sudo chmod 666 /dev/video0
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/projects/trial_b.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
source /home/jaram/myenv/bin/activate
sudo apt update
sudo apt install python3-venv
python3 -m venv /home/jaram/myenv
source /home/jaram/myenv/bin/activate
pip install RPi.GPIO
python
>>> import RPi.GPIO as GPIO
>>> print(GPIO)
<module 'RPi.GPIO' from '/home/jaram/myenv/lib/python3.9/site-packages/RPi/GPIO.cpython-39-arm-linux-gnueabihf.so'>
>>> exit()
python /home/jaram/projects/trial_b.py
/home/jaram/myenv/bin/python /home/jaram/projects/trial_b.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/cv_env/test.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/projects/trial_b.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/cv_env/k.py
source /home/jaram/cv_env/bin/activate
pip install flask
pip list
source /home/jaram/cv_env/bin/activate
pip show flask
which python
python /home/jaram/cv_env/k.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/cv_env/k.py
/home/jaram/cv_env/bin/python /home/jaram/cv_env/d.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
python /home/jaram/app.py
ls-al
ls -al
chmod 777 /home/jaram/static
python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
ls /dev/video*
fuser /dev/video0
sudo kill -9 <PID>
fuser /dev/video0
sudo kill -9 <10936m>
sudo kill -9 <10936>
sudo kill -9 10936
/home/jaram/cv_env/bin/python /home/jaram/app.py
sudo chmod 666 /dev/video0
v4l2-ctl --list-devices
/home/jaram/cv_env/bin/python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
v4l2-ctl --list-devices
/home/jaram/cv_env/bin/python /home/jaram/app.py
python /home/jaram/app.py
/home/jaram/cv_env/bin/python /home/jaram/app.py
sudo lsof -i :5000
/home/jaram/cv_env/bin/python /home/jaram/app.py
git init
git add .
