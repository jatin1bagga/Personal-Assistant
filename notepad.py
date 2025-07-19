import os
import pyautogui
import time

def open_notepad():
    os.system("start notepad")
    
def close_notepad(speakfunc):    
    os.system("taskkill /f /im notepad.exe")
    
def write_on_notepad(text):
    time.sleep(2) 
    pyautogui.typewrite(text + '\n')