import unittest
from draw import Canvas

class DrawTestCase(unittest.TestCase):
    """Tests for `draw.py`."""

    def setUp(self):
        self.canvas = Canvas()

    def test_create_canvas(self):
        """It is possible to create a canvas?"""

        #test errors
        self.assertFalse(self.canvas.execute("C"))
        self.assertFalse(self.canvas.execute("C z"))
        self.assertFalse(self.canvas.execute("C z z"))
        self.assertFalse(self.canvas.execute("C z 2"))
        self.assertFalse(self.canvas.execute("C 2 a"))
        
        #test valid creation
        self.assertTrue(self.canvas.execute("C 3 3"))
        self.assertEqual(self.canvas.size(), (3,3))
        self.assertTrue(self.canvas.execute("C 10 20"))
        self.assertEqual(self.canvas.size(), (10,20))

if __name__ == '__main__':
    unittest.main()
