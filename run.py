#!/usr/bin/python
from subprocess import Popen
import subprocess
import os
import time
#
while True:
    try:
        deamon = subprocess.Popen(['/usr/bin/python', '/opt/update-google-doc.py'])
        time.sleep(300)
        deamon.kill()
    except:
        pass
    
    
