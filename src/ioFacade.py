from pymouse import PyMouse
from pykeyboard import PyKeyboard
from gameData import xCoords, yCoords, originX, originY
import time
import pyautogui
import math


def getTilePosition((tileX, tileY), xCoords=xCoords, yCoords=yCoords):
    """
        Given (x,y) pair for a tile's location on the grid, 
        returns the tile's location on the screen
    """
    return (originX+xCoords[tileX], originY+yCoords[tileY])


def switchFocus(n=1, sleepTime=0.1):
    """ Performs alt tab, can skip n-1 applications """
    k = PyKeyboard()
    k.press_key(k.alt_key)
    time.sleep(sleepTime)
    for i in range(n):
        k.tap_key(k.tab_key)
        time.sleep(sleepTime)
    k.release_key(k.alt_key)


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def speedOfMouseMovement(origin, dest, unitSpeed=0.002):
    return distance(origin, dest) * unitSpeed


def autoGuiMouseDrag(origin, dest):
    pyautogui.moveTo(origin[0], origin[1])
    pyautogui.dragTo(dest[0], dest[1], 
            speedOfMouseMovement(origin, dest), 
            button='left')
