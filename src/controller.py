import gameData as gD
import matcher
import screenshot as ssLib
import ioFacade

import time

def screenshotOfGameGrid():
    return ssLib.getScreenshot(originX=gD.originX,
            originY=gD.originY,
            width=gD.imagewidth,
            height=gD.imageheight)
    
def screenshotToGrid(screenshot):
    pixels = screenshot
    grid = []
    for y in gD.yCoords:
        for x in gD.xCoords:
            grid.append(pixels[matcher.ijToIndex(x,y,gD.imagewidth)])
    return grid


def performMatch(grid, gameRunning=True):
    matchFound, dragFromTile, dragToTile = matcher.findMatch(grid)
    print("matchFound: ", matchFound)
    print("dragFromTile: ", dragFromTile)
    print("dragToTile: ", dragToTile)
    if matchFound and gameRunning:
        ioFacade.autoGuiMouseDrag(
                ioFacade.getTilePosition(dragFromTile),
                ioFacade.getTilePosition(dragToTile))

if __name__ == '__main__':
    gameRunning = True
    ss = None
    li = []
    allowedNumberOfRetries = 5
    retryCount = 0
    allowedNumberOfUnknowns = 10
    if gameRunning:
        ss = screenshotToGrid(screenshotOfGameGrid())
    else:
        ss = screenshotToGrid(ssLib.getPretendScreenshot("../img/sweet.png"))
    print("GRID BEFORE CHANGE")
    while retryCount != allowedNumberOfRetries:
        ss = screenshotToGrid(screenshotOfGameGrid())
        if gD.numberOfUnknownTiles(ss) <= allowedNumberOfUnknowns:
            gD.prettyPrintGrid(gD.rgb_to_tile_names(ss))
            performMatch(ss, gameRunning)
            time.sleep(0.1)
            ioFacade.switchFocus()
            time.sleep(0.1)
            retryCount = 0
        else:
            print("Too many unrecognised tiles. Will try again in one second")
            retryCount = retryCount + 1
            time.sleep(1)
