import numpy as np
import re

class Canvas():


    _canvas = None
    _quit   = False

    def __init__(self):
        self._canvas = np.zeros(shape = (0,0))
        self._quit = False

    def is_canvas(self):
        if self.size() == (0,0):
            return False
        else:
            return True
    def is_quit(self):
        return self._quit

    def execute(self, command):
        match = re.match("([CLRBQclrbq])\s?(\d)?\s?(\d)?\s?(\w)?\s?(\d)?", command)
        if match:
            if match.group(1).lower() == 'c':
                try:
                    w = int(match.group(2))
                    h = int(match.group(3))
                    return True
                except:
                    print('Invalid parameters for C')
                    print('Usage: C w h, where both w and h are integers, the former is the width and h is the height')
                    return False
            if match.group(1).lower() == 'l':
                pass
            if match.group(1).lower() == 'r':
                pass
            if match.group(1).lower() == 'b':
                pass
            if match.group(1).lower() == 'q':
                pass
        return 'NOP'
    def size(self):
        return self._canvas.shape
    def create(self, w, h):
        self._canvas = np.zeros(shape = (w,h))

    def draw_canvas(self):
        if self.is_canvas():
            pass


if __name__ == "__main__":


    canvas = Canvas()

    

    while not canvas.is_quit():
        if not canvas.is_canvas():
            print('Hello!')
            print('Please use the following command to create a new canvas')
            quit = True
        inp = input('enter command: ')

        canvas.execute(inp)
        canvas.draw_canvas()
