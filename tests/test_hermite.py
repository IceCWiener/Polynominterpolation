import unittest
from hermite import Hermite
from utility import Utility


class TestHermite(unittest.TestCase):
    def test_should_return_x_list(self):
        util = Utility()
        xy_list = [(2, 3), (5, 7)]
        expected = [2, 5]
        result = util.get_x_values(xy_list)
        self.assertEqual(expected, result)

    def test_should_return_coefficients(self):
        hermite = Hermite()
        x_values = [1, 1, 2]
        y_values = [1, 1, 3]
        expected = [1.0, 4.0, -2.0]
        xy_values = [(1, 1), (1, 4), (2, 3)]
        result = hermite.hermite_divided_differences(
            x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_two_sampling_points(self):
        hermite = Hermite()
        x_values = [1, 2]
        y_values = [1, 3]
        expected = [1.0, 2.0]
        xy_values = [(1, 1), (2, 3)]
        result = hermite.hermite_divided_differences(
            x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_coefficients_when_one_sampling_point(self):
        hermite = Hermite()
        x_values = [4]
        y_values = [5]
        expected = [5.0]
        xy_values = [(4, 5)]
        result = hermite.hermite_divided_differences(
            x_values, y_values, xy_values)
        self.assertEqual(expected, result)

    def test_should_return_divided_differences_when_mathepeter_sampling_points(self):
        hermite = Hermite()
        x_values = [1, 1, 2, 2, 2]
        y_values = [1, 1, 3, 3, 3]
        expected = [1.0, 4.0, -2.0, 1.0, 1.0]
        sampling_points = [(1, 1), (1, 4), (2, 3), (2, 1), (2, 2)]
        self.assertEqual(expected, hermite.hermite_divided_differences(
            x_values, y_values, sampling_points))

    def test_should_return_y_values_when_mathepeter_sampling_points(self):
        util = Utility()
        x_values = [1, 1, 2, 2, 2]
        expected = [1, 1, 3, 3, 3]
        sampling_points = [(1, 1), (1, 4), (2, 3), (2, 1), (2, 2)]
        self.assertEqual(expected, util.get_y_values(sampling_points))


if __name__ == '__main__':
    unittest.main()
