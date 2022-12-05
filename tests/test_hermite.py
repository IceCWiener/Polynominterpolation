import unittest
from hermite import Hermite


class TestHermite(unittest.TestCase):
    def test_should_return_x_list(self):
        hermite_mali = Hermite()
        xy_list = [(2, 3), (5, 7)]
        expected = [2, 5]
        result = hermite_mali.get_x_value_list(xy_list)
        self.assertEqual(expected, result)

    def test_should_return_coefficients(self):
        hermite_mali = Hermite()
        x_values = [1, 1, 2]
        y_values = [1, 1, 3]
        expected = [1.0, 4.0, -2.0]
        xy_values = [(1, 1), (1, 4), (2, 3)]
        result = hermite_mali.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_two_sampling_points(self):
        hermite_mali = Hermite()
        x_values = [1, 2]
        y_values = [1, 3]
        expected = [1.0, 2.0]
        xy_values = [(1, 1), (2, 3)]
        result = hermite_mali.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_one_sampling_point(self):
        hermite_mali = Hermite()
        x_values = [4]
        y_values = [5]
        expected = [5.0]
        xy_values = [(4, 5)]
        result = hermite_mali.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
