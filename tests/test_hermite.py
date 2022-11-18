import unittest
from hermite_model import Hermite


class TestHermite(unittest.TestCase):
    # def test_should_return_polynom_when_input_is_sampling_points(self):
    #     user_input = [(1, 1), (1, 4), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = "1 + 4(x-1) - 2(x-1)(x-1)"
    #     result = hermite.create_polynom()
    #     self.assertEqual(expected, result)

    # def test_should_return_multiplies_when_input_is_sampling_points(self):
    #     user_input = [(1, 1), (1, 4), (2, 3)]
    #     hermite = Hermite(user_input)
    #     expected = [1, 4, -2]
    #     result = hermite.divided_differences()
    #     self.assertEqual(expected, result)


    def test_should_return_true_if_we_divide_by_zero(self):
        sampling_points = [(1, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        expected = True
        result = hermite.would_divide_by_zero(sampling_points)
        self.assertEqual(expected, result)

    def test_should_return_false_if_we_dont_divide_by_zero(self):
        sampling_points = [(3, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        expected = False
        result = hermite.would_divide_by_zero(sampling_points)
        self.assertEqual(expected, result)

    def test_should_return_multiplier(self):
        sampling_points = [(3, 1), (1, 4)]
        hermite = Hermite(sampling_points)
        expected = 2
        coordinates = [(1, 1), (2, 3)]
        result = hermite.generate_multiplier(coordinates[0], coordinates[1])
        self.assertEqual(expected, result)

    def test_should_return_coordinate_list(self):
        sampling_points_list = [(1, 1), (1, 4)]
        hermite = Hermite(sampling_points_list)
        expected = [(1, 1), (1, 1)]
        result = hermite.generate_coordinates_list(sampling_points_list)
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
