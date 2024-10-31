# lights

Headless RaspberryPi lights programming for Halloween costume

To get to work on raspy, had to run the following:
```
sudo python3 -m venv /home/pi/root_env
sudo /home/pi/root_env/bin/pip install -r requirements.txt
sudo /home/pi/root_env/bin/python3 lights.py
```

To create a session that will persist after ssh terminates, run the following
```
tmux new -s my_session
tmux detach -s my_session
```
Later can reattach with:
```
tmux attach -t my_session
```
