#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os
import subprocess
 
bit = os.uname().machine
changes = subprocess.getoutput("git status --porcelain")
 
if changes:
    os.system("git reset --hard")
    os.system("git clean -fd")
    os.system("git pull")
 
os.system("chmod 777 *")
 
if '64' in bit:
    import FX_FILE
else:
    os.system("clear")
    print("TOOL NOT AVAILABLE FOR 32 BIT DEVICE")
 
