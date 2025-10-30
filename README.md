# lights

Headless RaspberryPi lights programming for Halloween costume

Pins for lights  
power (red) goes on pin 2 (1st pin on outside)  
data (blue) goes on pin 6 (3rd pin on outside)  
white (ground) goes on pin 12 (6th on outside)  

Setup script:  
```
sudo snap install tmux  --classic
#To create a session that will persist after ssh terminates, run the following
tmux new -s my_session
ssh pi@raspberrypi.local
git clone https://github.com/wjewell3/lights.git
cd lights
sudo apt update
sudo apt install python3.13-dev
sudo python3 -m venv venv
source venv/bin/activate
sudo /home/pi/lights/venv/bin/pip install -r requirements.txt
sudo /home/pi/lights/venv/bin/python bee.py
# dettach from session
Ctrl + b  then  d
# reattach
tmux attach -t my_session
```

Initiate later:  
```
tmux new -s my_session
ssh pi@raspberrypi.local
cd lights
source venv/bin/activate
sudo /home/pi/lights/venv/bin/python bee.py
Ctrl + b  then  d
```