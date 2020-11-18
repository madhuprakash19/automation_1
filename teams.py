#win10 pythoncode
import pyautogui as pg
from datetime import datetime
import time
i=1
while(i):
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    print(current_time)
    #i=0
    if current_time=="14:52":
        i=0
        pg.hotkey('ctrl','shift','b')
    time.sleep(15)
