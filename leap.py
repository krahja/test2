import time, pyautogui
from datetime import datetime
from mss import mss
from PIL import Image
print(pyautogui.position())
while True:
    time.sleep(55)
    pyautogui.click(x=85,y=105)
    time.sleep(5)
    now = datetime.strftime(datetime.now(), "%H")
    now = int(now)
    if now >= 5 and now <= 23:
        sct = mss()
        name = 's.png'
        f = sct.shot(output=name)
        im = Image.open(name)
        pix = im.load()
        if pix[75,239][0] == 255:
            print(pix[pyautogui.position()][0])
            pyautogui.click(x=192,y=244)
            #action
            time.sleep(60*3)
    #pyautogui.click(x=1135,y=862)
