# pip3 install pyautogui

import time
import pyautogui


pyautogui.dragRel(0, 300, .25)


pyautogui.moveTo(pyautogui.size().width/2,
                 pyautogui.size().height/3,
                 duration=.1)

pyautogui.dragRel(300, 0, .25)


pyautogui.moveTo(pyautogui.size().width/2,
                 pyautogui.size().height/3,
                 duration=.1)

pyautogui.dragRel(0, 300, .25)


def resetPosition():
    pyautogui.moveTo(pyautogui.size().width/2,
                     pyautogui.size().height/3,
                     duration=.1)


def main():
    print("waiting 1 second... switch to game window")
    time.sleep(1)


main()
