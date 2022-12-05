import unittest
from hermite import Hermite


class TestHermite(unittest.TestCase):
    def test_should_return_x_list(self):
        hermite = Hermite()
        xy_list = [(2, 3), (5, 7)]
        expected = [2, 5]
        result = hermite.get_x_value_list(xy_list)
        self.assertEqual(expected, result)

    def test_should_return_coefficients(self):
        hermite = Hermite()
        x_values = [1, 1, 2]
        y_values = [1, 1, 3]
        expected = [1.0, 4.0, -2.0]
        xy_values = [(1, 1), (1, 4), (2, 3)]
        result = hermite.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_two_sampling_points(self):
        hermite = Hermite()
        x_values = [1, 2]
        y_values = [1, 3]
        expected = [1.0, 2.0]
        xy_values = [(1, 1), (2, 3)]
        result = hermite.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_one_sampling_point(self):
        hermite = Hermite()
        x_values = [4]
        y_values = [5]
        expected = [5.0]
        xy_values = [(4, 5)]
        result = hermite.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_sampling_point_y_value_zero(self):
        hermite = Hermite()
        x_values = [1, 2, 10]
        y_values = [1, 0, 4]
        expected = [1/6, -3/2, 7/3]
        xy_values = [(1, 1), (2, 0), (10, 4)]
        result = hermite.divided_differences(x_values, y_values, xy_values)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
