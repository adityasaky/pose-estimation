#!/bin/bash

apt-get update
apt-get install python3-pip python3-dev
pip3 install --upgrade pip
pip3 install tensorflow-gpu
pip3 install keras
pip3 install numpy
pip3 install opencv-python
