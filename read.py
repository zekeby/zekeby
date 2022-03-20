#!/usr/bin/python

import time
import os

while True: 
    f1 = open('/var/log/auth.log', 'r+')
    data1 = f1.read()
#    print(data1)
    f1.close()
    time.sleep(1)
    f2 = open('/var/log/auth.log', 'r+')
    data2 = f2.read()
#    print(data2)
    f2.close()

    if data1 != data2:
        os.system("tail -n 1 /var/log/auth.log | grep ssh")
