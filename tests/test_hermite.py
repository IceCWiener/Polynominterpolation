import unittest
from hermite import Hermite
import numpy as np


class TestHermite(unittest.TestCase):
    def test_should_return_x_list(self):
        hermite_mali = Hermite()
        xy_list = [(2, 3), (5, 7)]
        expected = [2, 5]
        result = hermite_mali.get_x_value_list(xy_list)
        self.assertEqual(expected, result)

    def test_should_return_coefficients(self):
        hermite_mali = Hermite()
        x_values = (1, 1, 3)
        y_values = (4, 3, 2)
        expected = [4.0, 0.0, -0.25]
        xy_values = []
        result = hermite_mali.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
