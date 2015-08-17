from entrypoint2 import entrypoint
from pyscreenshot import grab

'''
    Just take screenshots and display them
'''


@entrypoint
def show(backend='auto'):
    if backend == 'auto':
        backend = None
    im = grab(bbox=(300, 180, 1000, 800), backend=backend)
    im.show()
