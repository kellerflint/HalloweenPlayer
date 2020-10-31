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
    resetPosition()
    pyautogui.dragRel(300, 0, .12)


def drawLineY():
    resetPosition()
    pyautogui.dragRel(0, 300, .12)


def drawVUp():
    resetPosition()
    pyautogui.mouseDown()
    pyautogui.moveRel(150, 300, .06)
    pyautogui.moveRel(150, -300, .06)
    pyautogui.mouseUp()


def drawVDown():
    resetPosition()
    pyautogui.moveRel(0, 300, 0)
    pyautogui.mouseDown()
    pyautogui.moveRel(150, -300, .06)
    pyautogui.moveRel(150, 300, .06)
    pyautogui.mouseUp()


drawings = [drawLineX, drawLineY, drawVUp, drawVDown]


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
