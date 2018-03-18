import unittest
import numpy as np
from draw import Canvas



class DrawTestCase(unittest.TestCase):
    """Tests for `draw.py`."""

    def setUp(self):
        self.canvas = Canvas()

    def test_create_canvas(self):
        """It is possible to create a canvas?"""

        #test input errors
        self.assertEqual(self.canvas.execute("C"), "CINV")
        self.assertEqual(self.canvas.execute("C z"), "CINV")
        self.assertEqual(self.canvas.execute("C z z"), "CINV")
        self.assertEqual(self.canvas.execute("C z 2"), "CINV")
        self.assertEqual(self.canvas.execute("C 2 z"), "CINV")
        
        #test valid creation
        self.assertTrue(self.canvas.execute("C 3 3"))
        self.assertEqual(self.canvas.size(), (3,3))
        self.assertTrue(self.canvas.execute("C 10 20"))
        self.assertEqual(self.canvas.size(), (10,20))
        self.assertTrue(self.canvas.execute("C 10 2  "))
        self.assertEqual(self.canvas.size(), (10,2))
        self.assertTrue(self.canvas.execute("C  1  2   "))
        self.assertEqual(self.canvas.size(), (1,2))

    def test_draw_line(self):
        """Let you draw a straight line?"""

        #test input errors
        self.assertEqual(self.canvas.execute("L"), "LINV")
        self.assertEqual(self.canvas.execute("L x x x x"), "LINV")
        self.assertEqual(self.canvas.execute("L x 2 3 4"), "LINV")
        self.assertEqual(self.canvas.execute("L 23 4 2 x"), "LINV")
        self.assertEqual(self.canvas.execute("L 2 2 2 x"), "LINV")

        #test out of range errors
        self.canvas.execute("C 3 3")
        self.assertEqual(self.canvas.execute("L 0 0 0 3"), "LRANGE")
        self.assertEqual(self.canvas.execute("L 1 1 1 4"), "LRANGE")

        #test not straight lines
        self.canvas.execute("C 9 9")
        self.assertEqual(self.canvas.execute("L 1 1 5 5"), "LSTR8L")

        #test line drawing
        self.canvas.execute("C 9 9")
        testarray = np.zeros((9, 9), str)

        testarray[1][1] = 'x'
        testarray[1][2] = 'x'
        testarray[1][3] = 'x'
        testarray[1][4] = 'x'
        testarray[1][5] = 'x'
        
        """
        testarray = np.array(
        [
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ], str)
        """

        testarray = np.array(
        [
        ['x','x','x','x','x','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ], str)

        self.canvas.execute("L 1 1 5 1")
        self.assertTrue(np.array_equal(self.canvas.get_canvas(), testarray))

        #test line drawing starting from the end to the beginning
        self.canvas.execute("C 9 9")
        self.canvas.execute("L 5 1 1 1")
        self.assertTrue(np.array_equal(self.canvas.get_canvas(), testarray))
    def test_draw_rectangle(self):
        """Can you draw a square?"""

        #test input errors
        self.assertEqual(self.canvas.execute("R"), "RINV")
        self.assertEqual(self.canvas.execute("R x x x x"), "RINV")
        self.assertEqual(self.canvas.execute("R x 2 3 4"), "RINV")
        self.assertEqual(self.canvas.execute("R 23 4 2 x"), "RINV")
        self.assertEqual(self.canvas.execute("R 2 2 2 x"), "RINV")

        #test out of range errors
        self.canvas.execute("C 3 3")
        self.assertEqual(self.canvas.execute("R 0 0 2 3"), "RRANGE")
        self.assertEqual(self.canvas.execute("R 1 1 2 4"), "RRANGE")

        #test square drawing
        self.canvas.execute("C 9 9")
        testarray = np.zeros((9, 9), str)

        testarray = np.array(
        [
        ['','x','x','x','x','','','',''],
        ['','x','','','x','','','',''],
        ['','x','x','x','x','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ], str)

        self.canvas.execute("R 2 1 5 3")
        self.assertTrue(np.array_equal(self.canvas.get_canvas(), testarray))
    
if __name__ == '__main__':
    unittest.main()
