from datatime import datatime
import os
import time

while True:
    os.system('cls')
    print(datatime.now().strftime("%H:%M:%S"))
    time.sleep(1)