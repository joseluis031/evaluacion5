from datetime import datetime
import os
import time

while True:
    os.system("cls")
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)