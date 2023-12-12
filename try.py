import pyautogui as gui
import time

def gs(x, y):
    gui.click(x,y)
    time.sleep(1)
    
print(gui.position())
gui.click(-1866, 134)
time.sleep(0.05)
gui.click(-1866, 134)
time.sleep(15)
gui.click(-239, 479)