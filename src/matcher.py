import screenshot
from collections import Counter
import gameData as data

originX, originY = 300, 180
imagewidth, imageheight = 1000 - originX, 800 - originY
gameRunning = False


def shiftByN(grid, lineIndex, isRow=False, shiftSize=1, rowWidth=data.gridwidth, colHeight=data.gridheight):
    # ensure all indexes are addressable in list
    assert(len(grid) >= rowWidth*colHeight)

    gridCopy = data.copyList(grid)

    if isRow:
        for shift in range(shiftSize):
            temp = gridCopy[lineIndex]
            for i in range(colHeight - 1):
                gridCopy[lineIndex+rowWidth*i] = gridCopy[lineIndex+rowWidth*(i+1)]
            gridCopy[lineIndex+(colHeight-1)*rowWidth] = temp
    else:
        for shift in range(shiftSize):
            temp = gridCopy[lineIndex*rowWidth]
            for i in range(rowWidth - 1):
                gridCopy[lineIndex*rowWidth+i] = gridCopy[lineIndex*rowWidth+i+1]
            gridCopy[(lineIndex+1)*rowWidth-1] = temp
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
    # First check the set of horizontal shifts for possible matches
    
    for row in reversed(range(colHeight)):
        for pos in range(rowWidth - 1):
            alteredCopyOfGrid = shiftByN(grid=data.copyList(grid),
                    lineIndex=row,
                    isRow=False,
                    shiftSize=pos+1)  # don't bother checking unaltered state for match
                            # Should really make sure I am checking every 
                            # pos that I think I am
            #print("CURRENT FORM OF GRID COPY", "row", row, "pos", pos)
            #data.prettyPrintGrid(data.rgb_to_tile_names(alteredCopyOfGrid))
            if (foundMatchOnGrid(alteredCopyOfGrid)):
                print("GRID AFTER CHANGE")
                data.prettyPrintGrid(data.rgb_to_tile_names(alteredCopyOfGrid))
                # rowWidth - 1 to give the rightmost position
                # rowWidth - 1 - (pos+1) like the pos+1 above
                return True, (rowWidth-1, row), (rowWidth-1-(pos+1), row)
    

    # Then check the set of vertical shifts for possible matches
    for col in range(rowWidth):
        for pos in range(colHeight - 1):
            alteredCopyOfGrid = shiftByN(grid=data.copyList(grid),
                    lineIndex=col,
                    isRow=True,
                    shiftSize=pos+1)  # don't bother checking unaltered state for match
                            # Should really make sure I am checking every 
                            # pos that I think I am
            #print("CURRENT FORM OF GRID COPY", "row", row, "pos", pos)
            #data.prettyPrintGrid(data.rgb_to_tile_names(alteredCopyOfGrid))
            if (foundMatchOnGrid(alteredCopyOfGrid)):
                print("GRID AFTER CHANGE")
                data.prettyPrintGrid(data.rgb_to_tile_names(alteredCopyOfGrid))
                # colHeight - 1 to give the bottommost position
                # colHeight - 1 - (pos+1) like the pos+1 above
                return True, (col, colHeight-1), (col, colHeight-1-(pos+1))
    return False, None, None
