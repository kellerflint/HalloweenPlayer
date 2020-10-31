# Player for the halloween google doodle
# Press x to start the player
# Hold q to quit the player
#
# Dependencies:
#   pip3 install pyautogui
#   pip3 install keyboard


import time
import pyautogui
import keyboard


def resetPosition():
    pyautogui.moveTo(pyautogui.size().width/2,
                     pyautogui.size().height/3,
                     duration=.1)


def drawLineX():
    pyautogui.dragRel(300, 0, .25)
    resetPosition()


def drawLineY():
    pyautogui.dragRel(0, 300, .25)
    resetPosition()


drawings = [drawLineX, drawLineY]


def main():
    print("Switch to game window now. Press x to start the player and hold q to stop it.")

    startGame = False
    while not startGame:
        if keyboard.is_pressed('x'):
            startGame = True

    endGame = False
    while not endGame:
        for drawing in drawings:
            if keyboard.is_pressed('q'):
                print('Exiting...')
                endGame = True
                break
            drawing()


main()
