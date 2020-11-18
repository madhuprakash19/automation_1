#win10 pythoncode
#incomplete
import pyautogui
import time
import keyboard
import win32api,win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(757,463)[0] == 0:
        click(757,463)
    if pyautogui.pixel(890,463)[0] == 0:
        click(890,463)
    if pyautogui.pixel(1014,863)[0] == 0:
        click(1014,863)
    if pyautogui.pixel(1144,863)[0] == 0:
        click(1144,863)

    
    
