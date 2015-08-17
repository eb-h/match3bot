import screenshot
from collections import Counter
import gameData as data

originX, originY = 300, 180
imagewidth, imageheight = 1000 - originX, 800 - originY
gameRunning = False


def shiftRowByN(grid, rowIndex, shiftSize=1, rowWidth=data.gridwidth, colHeight=data.gridheight):
    """ Performs leftward shift """
    # ensure all indexes are addressable in list
    assert(len(grid) >= rowWidth*colHeight)

    gridCopy = data.copyList(grid)
    # CURRENTLY n^2 when it should be 2*n
    # Eric please please please fix this before showing people
    for shift in range(shiftSize):
        temp = gridCopy[rowIndex*rowWidth]
        for i in range(rowWidth - 1):
            gridCopy[rowIndex*rowWidth+i] = gridCopy[rowIndex*rowWidth+i+1]
        gridCopy[(rowIndex+1)*rowWidth-1] = temp
    return gridCopy


def ijToIndex(x, y, rowWidth=data.gridwidth):
    return x + rowWidth*y


def ijTriplet(grid, (a,b), (c,d), (e,f), rowWidth=data.gridwidth):
    return (grid[ijToIndex(a,b, rowWidth)],
            grid[ijToIndex(c,d, rowWidth)],
            grid[ijToIndex(e,f, rowWidth)])


def matchingTriplet((x, y, z)):
    return x == y and y == z


def checkForMatchAtPos(x, y, grid, rowWidth=data.gridwidth, colHeight=data.gridheight):
    """ Only checks above and to the left 
          x
          x
        xxo 
    """
    # ensure index is within bounds
    assert(x+y*rowWidth < len(grid))
    # should only be used from foundMatchOnGrid()
    assert(x >= 2 and y >= 2)
    if matchingTriplet(ijTriplet(grid, (x,y), (x-1,y), (x-2,y))):
        return True
    if matchingTriplet(ijTriplet(grid, (x,y), (x,y-1), (x,y-2))):
        return True
    return False


def foundMatchOnGrid(grid, rowWidth=data.gridwidth, colHeight=data.gridheight):
    """ 
        Currently very brute-forcy, much more than it 
        should be but very quick to make
    """
    # ensure grid is big enough to allow matches
    assert(rowWidth >= 2 and colHeight >= 2)
    for x in range(2, rowWidth):
        for y in range(2, colHeight):
            if checkForMatchAtPos(x, y, grid):
                return True
    return False


def findMatch(grid, rowWidth=data.gridwidth, colHeight=data.gridheight):
    """ 
        Checks if shifting any rows to the left causes a vertical match 
        Should return xy pos and how much to shift by    
    """
    for row in range(colHeight):
        for pos in range(rowWidth - 1):
            alteredCopyOfGrid = shiftRowByN(data.copyList(grid),
                    row,
                    pos+1,  # don't bother checking unaltered state for match
                            # Should really make sure I am checking every 
                            # pos that I think I am
                    rowWidth)
            #print("CURRENT FORM OF GRID COPY", "row", row, "pos", pos)
            #data.prettyPrintGrid(data.rgb_to_tile_names(alteredCopyOfGrid))
            if (foundMatchOnGrid(alteredCopyOfGrid)):
                print("GRID AFTER CHANGE")
                data.prettyPrintGrid(data.rgb_to_tile_names(alteredCopyOfGrid))
                # rowWidth - 1 to give the rightmost position
                # rowWidth - 1 - (pos+1) like the pos+1 above
                return True, (rowWidth-1, row), (rowWidth-1-(pos+1), row)
    return False, None, None

'''
if __name__ == '__main__':
    ss = None
    li = []
    if gameRunning:
        ss = screenshot.getScreenshot(originX=originX, originY=originY, width=imagewidth, height=imageheight)
    else:
        ss = screenshot.getPretendScreenshot("../img/sweet.png")
    print(data.rgb_to_tile_names(ss))
    """
    for x in xs:
        for y in ys:
            li.append(screenshot.specificPixel(ss, 
                data.xCoords, 
                data.yCoords, 
                imagewidth, 
                imageheight))
    print(Counter(li))

    """ 
'''