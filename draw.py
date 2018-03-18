import numpy as np
import re

class Canvas():


    _canvas = None
    _quit   = False

    def __init__(self):
        self._canvas = np.zeros((0,0), str)
        self._quit = False

    def is_canvas(self):
        if self.size() == (0,0):
            return False
        else:
            return True
    def is_quit(self):
        return self._quit

    def get_canvas(self):
        return self._canvas


    def execute(self, command):
        match = re.match("([CLRBQclrbq])\s*(\d*)?\s*(\d*)?\s*(\w*)?\s*(\d*)?", command)
        if match:
            if match.group(1).lower() == 'c':
                try:
                    w = int(match.group(2))
                    h = int(match.group(3))
                    self.create(w,h)
                    return True
                except:
                    return "CINV"
            if match.group(1).lower() == 'l':
                try:
                    x1 = int(match.group(2))
                    y1 = int(match.group(3))
                    x2 = int(match.group(4))
                    y2 = int(match.group(5))
                except:
                    return "LINV"
                w, h = self.size()
                if w <= (x1 or x2) or h <= (y1 or y2):
                    return ("LRANGE")

                if x1 == x2 or y1 == y2:
                    self.draw_line(x1,y1,x2,y2)
                    return True
                else:
                    return "LSTR8L"
            if match.group(1).lower() == 'r':
                try:
                    x1 = int(match.group(2))
                    y1 = int(match.group(3))
                    x2 = int(match.group(4))
                    y2 = int(match.group(5))
                except:
                    return "RINV"
                w, h = self.size()
                if w <= (x1 or x2) or h <= (y1 or y2):
                    return ("RRANGE")

                self.draw_line(x1,y1,x2,y1)
                self.draw_line(x1,y1,x1,y2)
                self.draw_line(x1,y2,x2,y2)
                self.draw_line(x2,y1,x2,y2)

                return True
            if match.group(1).lower() == 'b':
                pass
            if match.group(1).lower() == 'q':
                pass
        return 'NOP'
    def size(self):
        h, w = self._canvas.shape
        return (w, h)
    def create(self, w, h):
        self._canvas = np.zeros((h, w), str)


    def draw_line(self, x1, y1, x2, y2, character = 'x'):
        if x1 > x2:
            aux = x1
            x1 = x2
            x2 = aux
        if y1 > y2:
            aux = y1
            y1 = y2
            y2 = aux

        if x1 == x2:
            for i in range(y1, y2 + 1):
                self._canvas[i][x1] = character
        elif y1 == y2:
            for i in range(x1, x2 + 1):
                self._canvas[y1][i] = character

    def draw_canvas(self):
        if self.is_canvas():
            w, h = self.size()
            for x in range(0, h+2):
                if x == 0 or x == h+1:
                    print('-', end = '')
                else:
                    print('|', end = '')
                for y in range(0,w):
                    if x == 0 or x == h+1:
                        print('-', end = '')
                    else:
                        character = self._canvas[x-1][y]
                        if character == '':
                            character = ' '
                        print(character, end = '')
                if x == 0 or x == h+1:
                    print('-')
                else:
                    print('|')
            print()


if __name__ == "__main__":


    canvas = Canvas()

    

    while not canvas.is_quit():
        if not canvas.is_canvas():
            print('Hello!')
            print('Please use the following command to create a new canvas')
            quit = True
        inp = input('enter command: ')

        result = canvas.execute(inp)
        if result == True:
            pass
        else:
            if result == "CINV":
                print('Invalid parameters for C')
                print('Usage: C w h, where both w and h are integers, the former is the width and h is the height')
            else:
                print(result)
        canvas.draw_canvas()
