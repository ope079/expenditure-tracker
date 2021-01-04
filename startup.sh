#!/bin/bash

sudo apt update
sudo apt-get install python3
sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# pytest goes here
sudo tests/test_unit.py --cov=application --cov-report term-missing --disable-warnings

sudo mkdir /opt/expenditure-tracker
sudo chown -R jenkins /opt/expenditure-tracker

sudo systemctl daemon-reload
sudo systemctl stop expenditure-tracker.service
sudo systemctl start expenditure-tracker.service

