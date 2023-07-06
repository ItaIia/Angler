#Unfinished...
import pyautogui
import win32gui
import time
import sys

dialog_image = 'E.png'
dialog_string = 'E'
key_name = 'e'
screenWidth, screenHeight = pyautogui.size()
print("Starting Anglr")
count = 0
while True:

    c = (count+1)
    pyautogui.locateOnScreen(dialog_image)
    LOC = pyautogui.locateOnScreen(dialog_image, confidence=0.5)
    #currentMouseX, currentMouseY = pyautogui.position()
    #print(f"Mouse X Axis: {currentMouseX}")
    #print(f"Mouse Y Axis: {currentMouseY}")
    color = pyautogui.pixel(1120,982)
    color2 = pyautogui.pixel(1206,982)
    color2a = pyautogui.pixel(1203,982)
    color2b = pyautogui.pixel(1209,982)
    #MouseXY = (f"X: {currentMouseX} Y: {currentMouseY} | Color1 = {color} | Color2: {color2}")
    #Cinfo = f"{color} | {color2} - Count: {count}"
    #sys.stdout.write( '%s\r' % Cinfo)
   # sys.stdout.flush()
    
    if color2 == (59, 59, 59):
        pyautogui.keyDown(key_name)
        pyautogui.keyUp(key_name)
        print(f"1 Attempted Catch {c}")
        
    if color2a == (59, 59, 59):
        pyautogui.keyDown(key_name)
        pyautogui.keyUp(key_name)
        print(f"2 Attempted Catch {c}")
        
    if color2b == (59, 59, 59):
        pyautogui.keyDown(key_name)
        pyautogui.keyUp(key_name)
        print(f"3 Attempted Catch {c}")
    if color == (59, 59, 59):
        pyautogui.keyDown(key_name)
        time.sleep(.8)
        pyautogui.keyUp(key_name)
