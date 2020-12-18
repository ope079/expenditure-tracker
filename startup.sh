#!/bin/bash
cd /opt/expenditure-tracker
sudo mkdir /expenditure-tracker
sudo chown -R /expenditure-tracker
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 app.py


