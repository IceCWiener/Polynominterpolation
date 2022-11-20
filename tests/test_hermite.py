import unittest
from hermite import Hermite
from coordinate import Coordinate


class TestHermite(unittest.TestCase):
    def test_should_return_true_if_we_divide_by_zero(self):
        sampling_points = [(1, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        hermite.set_coordinates_list()
        expected = True
        result = hermite.is_same_x_value(hermite.coordinates_list[0], hermite.coordinates_list[1])
        self.assertEqual(expected, result)

    def test_should_return_false_if_we_dont_divide_by_zero(self):
        sampling_points = [(3, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        hermite.set_coordinates_list()
        expected = False
        result = hermite.is_same_x_value(hermite.coordinates_list[0], hermite.coordinates_list[1])
        self.assertEqual(expected, result)

    def test_should_return_coordinates_list(self):
        sampling_points_list = [(1, 1), (1, 4), (2, 3)]
        hermite = Hermite(sampling_points_list)
        expected = [(1, 1), (1, 1), (2, 3)]
        hermite.set_coordinates_list()
        result = hermite.get_coordinates_list_as_list_of_tuples()
        self.assertEqual(expected, result)

    # def test_should_return_polynom_when_input_is_sampling_points(self):
    #     user_input = [(1, 1), (1, 4), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = "1 + 4(x-1) - 2(x-1)(x-1)"
    #     result = hermite.create_polynom()
    #     self.assertEqual(expected, result)

    # def test_should_return_multiplier_when_input_is_2_coordinates(self):
    #     user_input = [(1, 1), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = 2.0
    #     coordinate_list = hermite.get_coordinates_list()
    #     result = hermite.get_multiplier(coordinate_list[0], coordinate_list[1])
    #     self.assertEqual(expected, result)


    def test_should_return_tuple_of_coordinate(self):
        coordinate = Coordinate(2, 3)
        self.assertEqual(coordinate.get_coordinate_tuple(), (2, 3))

    def test_should_return_true_when_two_consecutive_inputs_have_same_x_value(self):
        user_input = [(1, 1), (1, 2)]
        hermite = Hermite(user_input)
        self.assertEqual(hermite.is_same_x_value(Coordinate(1, 1), Coordinate(1, 2)), True)

    def test_should_return_coordinates_list(self):
        user_input = [(1, 1), (1, 4)]
        hermite = Hermite(user_input)
        expected = [(1, 1), (1, 1)]
        hermite.set_coordinates_list()
        result = hermite.get_coordinates_list_as_list_of_tuples()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_three_elements(self):
        user_input = [(1, 1), (1, 4), (7, 8)]
        hermite = Hermite(user_input)
        expected = [(1, 1), (1, 1), (7, 8)]
        hermite.set_coordinates_list()
        result = hermite.get_coordinates_list_as_list_of_tuples()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_four_elements(self):
        user_input = [(-2, 6), (3, -5), (7, 8)]
        hermite = Hermite(user_input)
        expected = [(-2, 6), (3, -5), (7, 8)]
        hermite.set_coordinates_list()
        result = hermite.get_coordinates_list_as_list_of_tuples()
        self.assertEqual(expected, result)

    def test_should_return_multiplier(self):
        sampling_points = [(1, 1), (2, 3)]
        hermite = Hermite(sampling_points)
        hermite.set_coordinates_list()
        coordinate_list = hermite.get_coordinates_list()
        expected = 2
        result = hermite.get_multiplier(coordinate_list[0], coordinate_list[1])
        self.assertEqual(expected, result)

    def test_should_return_multiplier_when_division_by_zero(self):
        sampling_points = [(1, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        hermite.set_coordinates_list()
        coordinate_list = hermite.get_coordinates_list()
        result = hermite.get_multiplier(coordinate_list[0], coordinate_list[1])
        expected = 4.0
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_correct_derivatives(self):
        sampling_points = [(1, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        hermite.set_coordinates_list()
        expected = 4
        second_coordinate = hermite.get_coordinates_list()[1]
        result = second_coordinate.get_derivative()[0]
        self.assertEqual(expected, result)


    def test_should_return_multiplier_when_division_by_zero_2(self):
        sampling_points = [(2, 7), (2, -100)]
        hermite = Hermite(sampling_points)
        hermite.set_coordinates_list()
        coordinate_list = hermite.get_coordinates_list()
        result = hermite.get_multiplier(coordinate_list[0], coordinate_list[1])
        expected = -100.0
        self.assertEqual(expected, result)

    # def test_should_return_multiplier_list(self):
    #     user_input = [(1, 1), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = [4]
    #     result = hermite.get_multipliers()
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
