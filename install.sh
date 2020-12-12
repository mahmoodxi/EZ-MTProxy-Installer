#!/bin/bash

apt update
apt install python3-pip git nload -y
wget https://github.com/mahmoodxi/EZ-MTProxy-Installer/raw/main/official-mtp.py
python3 official-mtp.py
