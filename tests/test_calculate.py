import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):


    def test_calc_circle_area(self):
        self.assertEqual(calc('circle', 'area', [2]), 12.566370614359172)
    def test_calc_square_perimeter(self):
        self.assertEqual(calc('square', 'perimeter', [4]), 16)
    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            calc('circle', 'volume', [2])
    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [2])
    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', ['invalid'])


if __name__ == "__main__":
    unittest.main()
