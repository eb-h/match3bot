xCoords = [10, 98, 186, 273, 362, 449, 537, 624]
yCoords = [ 7, 96, 183, 272, 359, 447, 534]
gridwidth, gridheight = 8, 7

originX, originY = 300, 180
imagewidth, imageheight = 1000 - originX, 800 - originY

tileColors = {'staff': (193, 41, 32), 
                'sword': (109, 140, 175),
                'key': (103, 186, 117),
                'wood': (171, 147, 122),
                'shield': (47, 117, 101),
                'stone': (110, 123, 145),
                'chest': (197, 136, 213)}


def rgb_to_tile_names(pixels):
    copy = pixels
    for i, item in enumerate(pixels):
        #valFound = False
        for tile_name, rgbVal in tileColors.items():
            if item == rgbVal:
                copy[i] = tile_name
                valFound = True
                break
        #if valFound == False:
            #copy[i] = "UNKNOWN"
    return copy


def prettyPrintGrid(grid):
    """ nicely prints out each element by tile_name """
    assert(len(grid) == gridwidth*gridheight)
    for i in range(gridheight):
        print('{:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8}'.format(
                grid[i*gridwidth], 
                grid[i*gridwidth+1], 
                grid[i*gridwidth+2], 
                grid[i*gridwidth+3], 
                grid[i*gridwidth+4], 
                grid[i*gridwidth+5], 
                grid[i*gridwidth+6], 
                grid[i*gridwidth+7]))


def copyList(li):
    return list(li)

