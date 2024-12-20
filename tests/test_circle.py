import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):


    def test_area(self):
        self.assertEqual(area(1), math.pi)
        with self.assertRaises(ValueError):
            area(0)
        with self.assertRaises(ValueError):
            area(-1)
    def test_perimeter(self):
        self.assertEqual(perimeter(1), 2 * math.pi)
        with self.assertRaises(ValueError):
            perimeter(0)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()
