#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os

# Check device architecture
bit = os.uname().machine

# Update repository (if applicable)
os.system('git pull')

# Set permissions for the .so file
os.system('chmod +x RANDOM.cython-312.so')

# Run the tool if 64-bit
if '64' in bit:
    if os.path.exists('RANDOM.cython-312.so'):
        os.system('python3.12 -c "import RANDOM.cython-312.so"')
    else:
        print('RANDOM.cython-312.so not found')
else:
    os.system('clear')
    print('TOOL NOT AVAILABLE FOR 32 BIT DEVICE')
