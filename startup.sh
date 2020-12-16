#!/bin/bash
sudo apt update
sudo apt-get install python3-venv


# Test Phase
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 app.py

# pytest goes here
pytest --cov ./application

# Deploy Phase


# Make the installation directory
sudo mkdir /opt/expenditure-tracker


# Give jenkins user permissions for the installation directory
sudo chown -R jenkins /opt/expenditure-tracker


sudo systemctl daemon-reload
sudo systemctl stop expenditure-tracker.service
sudo systemctl start expenditure-tracker.service
