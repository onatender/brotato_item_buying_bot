from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while not keyboard.is_pressed('esc'):
    data = pyautogui.locateOnScreen('tree.png',grayscale=True,confidence=0.8,region=(34,137,1223,245))
    if data != None:
        print("found, buying...")
        pyautogui.click(data.left+150,data.top+450)
    else:
        pyautogui.click(1200,50)