import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)
        with self.assertRaises(ValueError):
            area(0)
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        with self.assertRaises(ValueError):
            perimeter(0)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()
