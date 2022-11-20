import unittest
from coordinate_list import CoordinateList
from coordinate import Coordinate


class TestCoordinateList(unittest.TestCase):
    # def test_should_return_coordinate_list(self):
    #     expected = []
    #     result = app.collect_sampling_points()
    #     self.assertEqual(expected, result)

    def test_should_return_tuple_of_coordinate(self):
        coordinate = Coordinate(2, 3)
        self.assertEqual(coordinate.get_coordinate_tuple(), (2, 3))

    def test_should_return_true_when_two_consecutive_inputs_have_same_x_value(self):
        sampling_points_list = []
        coordinate_list = CoordinateList(sampling_points_list)
        self.assertEqual(coordinate_list.is_same_x_value(Coordinate(1, 1), Coordinate(1, 2)), True)

    def test_should_return_derivatives_list(self):
        coordinate = Coordinate(2, 3)
        coordinate.set_derivative(4, 1)
        coordinate.set_derivative(3, 2)
        expected = [(4, 1), (3, 2)]
        result = coordinate.get_derivatives()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list(self):
        user_input = [(1, 1), (1, 4)]
        expected = [(1, 1), (1, 1)]
        coordinate_list = CoordinateList(user_input)
        result = coordinate_list.get_coordinates()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_three_elements(self):
        user_input = [(1, 1), (1, 4), (7, 8)]
        expected = [(1, 1), (1, 1), (7, 8)]
        coordinate_list = CoordinateList(user_input)
        result = coordinate_list.get_coordinates()
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list_with_four_elements(self):
        user_input = [(-2, 6), (3, -5), (7, 8)]
        expected = [(-2, 6), (3, -5), (7, 8)]
        coordinate_list = CoordinateList(user_input)
        result = coordinate_list.get_coordinates()
        self.assertEqual(expected, result)
