
FROM selenium/standalone-firefox

WORKDIR /python-docker

COPY . .

COPY requirements.txt requirements.txt

RUN sudo apt-get update 
RUN sudo -H apt-get install --no-install-recommends -y python3 python3-dev python3-venv python3-pip python3-wheel build-essential

RUN pip install -r requirements.txt

#RUN apt-get install -qqy x11-apps x11vnc xvfb xorg
RUN sudo -H pip install flake8 pytest


CMD nohup ./firefox.sh;python3 app.py
