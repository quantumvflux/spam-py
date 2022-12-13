import pyautogui as pt
import time

n = input("nivel de spam:")
msg = input("mensajito:")
i = 0
time.sleep(10)

while i < int(n):
    pt.typewrite(msg)
    pt.press("enter")

    i+=1