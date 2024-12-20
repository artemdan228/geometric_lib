import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=1)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 1, 10)


if __name__ == "__main__":
    unittest.main()
