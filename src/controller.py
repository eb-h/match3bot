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


def performMatch(grid):
    matchFound, dragFromTile, dragToTile = matcher.findMatch(grid)
    print("matchFound: ", matchFound)
    print("dragFromTile: ", dragFromTile)
    print("dragToTile: ", dragToTile)
    if matchFound:
        ioFacade.autoGuiMouseDrag(
                ioFacade.getTilePosition(dragFromTile),
                ioFacade.getTilePosition(dragToTile))

if __name__ == '__main__':
    gameRunning = True
    ss = None
    li = []
    if gameRunning:
        ss = screenshotToGrid(screenshotOfGameGrid())
    else:
        ss = screenshotToGrid(ssLib.getPretendScreenshot("../img/sweet.png"))
    print("GRID BEFORE CHANGE")
    gD.prettyPrintGrid(gD.rgb_to_tile_names(ss))
    performMatch(ss)
    time.sleep(0.1)
    ioFacade.switchFocus()
