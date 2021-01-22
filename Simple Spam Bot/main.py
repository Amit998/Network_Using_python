import pyautogui
import time
import random


time.sleep(2)

# spam_text="This is spam text"


file=open('spam.txt','r').read()
file=file.splitlines()


for _ in range(20):
    pyautogui.typewrite(random.choice(file))
    pyautogui.press('enter')
    time.sleep(1)