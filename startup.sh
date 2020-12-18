#!/bin/bash
cd/opt/expenditure-tracker
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pyhton3 create.py
python3 app.py


