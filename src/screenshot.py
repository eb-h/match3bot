from pyscreenshot import grab
import Image


def getScreenshot(backend='auto', originX = 0, originY = 0, width=1280, height=800):
    if backend == 'auto':
        backend = None
    im = grab(bbox=(originX, originY, originX + width, originY + height), backend=backend)
    return list(im.getdata())


def getPretendScreenshot(ssLocation):
    im = Image.open(ssLocation)
    return list(im.getdata())


def specificPixel(screenshot, x, y, width, height):
    return screenshot[x + width*y]


if __name__ == '__main__':
    """ for quick verification """
    width, height = 1000, 800
    print(specificPixel(getScreenshot(originX = 300, originY = 180, width=width, height=height), 10, 8, width-300, height-180))
