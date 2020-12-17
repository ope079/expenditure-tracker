#!/bin/bash
sudo apt update
sudo apt-get install python3-venv



# Test Phase
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


# pytest goes here
pytest tests/test_unit.py --cov=application --cov-report term-missing --disable-warnings

# Deploy Phase


# Make the installation directory
sudo mkdir /opt/expenditure-tracker


# Give jenkins user permissions for the installation directory
sudo chown -R jenkins /opt/expenditure-tracker


sudo systemctl daemon-reload
sudo systemctl stop expenditure-tracker.service
sudo systemctl start expenditure-tracker.service

sleep 5


python3 -m pytest tests/test_int.py --cov=application --cov-report term-missing --disable-warnings