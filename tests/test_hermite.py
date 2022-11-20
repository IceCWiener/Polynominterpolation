import unittest
from hermite import Hermite
from coordinate import Coordinate


class TestHermite(unittest.TestCase):
    def test_should_return_true_if_we_divide_by_zero(self):
        sampling_points = [(1, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        expected = True
        result = hermite.would_divide_by_zero(sampling_points[0], sampling_points[1])
        self.assertEqual(expected, result)

    def test_should_return_false_if_we_dont_divide_by_zero(self):
        sampling_points = [(3, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        expected = False
        result = hermite.would_divide_by_zero(sampling_points[0], sampling_points[1])
        self.assertEqual(expected, result)

    def test_should_return_multiplier(self):
        sampling_points = [(3, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        expected = 2
        coordinates = [(1, 1), (2, 3)]
        result = hermite.get_multiplier(coordinates[0], coordinates[1])
        self.assertEqual(expected, result)

    # def test_should_return_coordinates_list(self):
    #     sampling_points_list = [(1, 1), (1, 4), (2, 3)]
    #     hermite = Hermite(sampling_points_list)
    #     expected = [(1, 1), (1, 1), (2, 3)]
    #     result = hermite.generate_coordinates_list()
    #     self.assertEqual(expected, result)

    # def test_should_return_polynom_when_input_is_sampling_points(self):
    #     user_input = [(1, 1), (1, 4), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = "1 + 4(x-1) - 2(x-1)(x-1)"
    #     result = hermite.create_polynom()
    #     self.assertEqual(expected, result)

    def test_should_return_multiplier_when_input_is_2_tuples(self):
        user_input = [(1, 1), (2, 3)]
        hermite = Hermite(user_input)
        expected = 2.0
        result = hermite.get_multiplier(user_input[0], user_input[1])
        self.assertEqual(expected, result)

    # def test_should_return_multiplier_list(self):
    #     user_input = [(1, 1), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = [4]
    #     result = hermite.get_multipliers()
    #     self.assertEqual(expected, result)

    def test_should_return_tuple_of_coordinate(self):
        coordinate = Coordinate(2, 3)
        self.assertEqual(coordinate.get_coordinate_tuple(), (2, 3))

    def test_should_return_true_when_two_consecutive_inputs_have_same_x_value(self):
        user_input = [(1, 1), (1, 2)]
        hermite = Hermite(user_input)
        self.assertEqual(hermite.is_same_x_value(Coordinate(1, 1), Coordinate(1, 2)), True)

    def test_should_return_derivatives_list(self):
        coordinate = Coordinate(2, 3)
        coordinate.set_derivative(4, 1)
        coordinate.set_derivative(3, 2)
        expected = [(4, 1), (3, 2)]
        result = coordinate.get_derivatives()
        self.assertEqual(expected, result)

    def test_should_return_coordinates_list(self):
        user_input = [(1, 1), (1, 4)]
        hermite = Hermite(user_input)
        expected = [(1, 1), (1, 1)]
        result = hermite.get_coordinates_list()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_three_elements(self):
        user_input = [(1, 1), (1, 4), (7, 8)]
        hermite = Hermite(user_input)
        expected = [(1, 1), (1, 1), (7, 8)]
        result = hermite.get_coordinates_list()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_four_elements(self):
        user_input = [(-2, 6), (3, -5), (7, 8)]
        hermite = Hermite(user_input)
        expected = [(-2, 6), (3, -5), (7, 8)]
        result = hermite.get_coordinates_list()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
