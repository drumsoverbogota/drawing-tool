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
        match = re.match("([CLRBQclrbq])\s*(\d+)?\s*(\d+)?\s*(\w+)?\s*(\d+)?", command)
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


                if (x1 > w or x2 > w) or (y1 > h or y2 > h):
                    return ("LRANGE")
                if (x1 == 0 or x2 == 0)  or (y1 == 0 or y2 == 0):
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
                if (x1 > w or x2 > w) or (y1 > h or y2 > h):
                    return ("RRANGE")
                if (x1 == 0 or x2 == 0)  or (y1 == 0 or y2 == 0):
                    return ("RRANGE")

                self.draw_line(x1,y1,x2,y1)
                self.draw_line(x1,y1,x1,y2)
                self.draw_line(x1,y2,x2,y2)
                self.draw_line(x2,y1,x2,y2)

                return True
            if match.group(1).lower() == 'b':
                try:
                    x = int(match.group(2))
                    y = int(match.group(3))
                    character = match.group(4)
                    if character == None:
                        character = ''
                except:
                    return "BINV"

                w, h = self.size()
                if x > w or y > h:
                    return ("BRANGE")
                if x == 0  or y == 0:
                    return ("BRANGE")

                original = self._canvas[y - 1][x - 1]
                if original != character:
                    self.fill(x, y, character, original)
                return True
            if match.group(1).lower() == 'q':
                pass
        return 'NOP'



    def size(self):
        h, w = self._canvas.shape
        return (w, h)
    def create(self, w, h):
        self._canvas = np.zeros((h, w), str)

    def fill(self, x, y, character, original):
        current = self._canvas[y - 1][x - 1]
        if original == current:
            self._canvas[y - 1, x - 1] = character
            if x - 1 > 0:
                self.fill(x - 1, y, character, original)
            if y - 1 > 0:
                self.fill(x, y - 1, character, original)
            w, h = self.size()
            if x + 1 <= w:
                self.fill(x + 1, y, character, original)
            if y + 1 <= h:
                self.fill(x, y + 1, character, original)

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
                self._canvas[i-1][x1-1] = character
        elif y1 == y2:
            for i in range(x1, x2 + 1):
                self._canvas[y1-1][i-1] = character

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
