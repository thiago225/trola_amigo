import pyautogui as py
import random
import time

time.sleep(10)

messagens = ["oi"]

for i in range(100):
    msg = random.choice(messagens)
    py.write(msg)
    py.press('enter')
