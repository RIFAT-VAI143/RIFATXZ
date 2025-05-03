#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os
bit = os.uname().machine
os.system('git checkout -- RANDOM && git pull')
os.system('chmod +x RANDOM')
if '64' in bit:
    os.system('./RANDOM')
else:
    os.system('clear')
    print('TOOL NOT AVAILABLE FOR 32 BIT DEVICE')