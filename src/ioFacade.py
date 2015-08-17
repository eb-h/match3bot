from pymouse import PyMouse
from pykeyboard import PyKeyboard
from gameData import xCoords, yCoords, originX, originY
import time
import pyautogui

'''
def mouseDrag(origin=(0,0), dest=(0,0), sleepTime=ioPauseTime):
    """ 
        sleeptime necessary or it's too fast for 
        linux to register a change 
    """
    m = PyMouse()
    m.move(origin[0], origin[1])
    time.sleep(sleepTime)
    m.press(origin[0], origin[1])
    time.sleep(sleepTime)
    m.move(origin[0], origin[1])
    time.sleep(sleepTime)
    m.release(dest[0], dest[1])
'''

def getTilePosition((tileX, tileY), xCoords=xCoords, yCoords=yCoords):
    """
        Given (x,y) pair for a tile's location on the grid, 
        returns the tile's location on the screen
    """
    return (originX+xCoords[tileX], originY+yCoords[tileY])


'''
def mouseDragByTile(tile1Pos, tile2Pos):
    mouseDrag(getTilePosition(tile1Pos),
            getTilePosition(tile2Pos))
'''

def switchFocus(n=1, sleepTime=0.1):
    """ Performs alt tab, can skip n-1 applications """
    k = PyKeyboard()
    k.press_key(k.alt_key)
    time.sleep(sleepTime)
    for i in range(n):
        k.tap_key(k.tab_key)
        time.sleep(sleepTime)
    k.release_key(k.alt_key)


def autoGuiMouseDrag(origin, dest):
    pyautogui.moveTo(origin[0], origin[1])
    pyautogui.dragTo(dest[0], dest[1], 1, button='left')
