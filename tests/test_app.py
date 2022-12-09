import unittest
from app import generate_polynom_with_brackets
from app import generate_multipliers

class TestApp(unittest.TestCase):
    def test_should_return_bracket_polynom_when_two_sampling_points(self):
        pyramid_matrix = [[1.0, 4.0], [1.0, 2.0], [3.0, 0.0]]
        x_values = [1, 1]
        expected = "1.0 + 4.0(x-1)"
        self.assertEqual(expected, generate_polynom_with_brackets(pyramid_matrix, x_values))

    def test_should_return_bracket_polynom_when_three_sampling_points(self):
        pyramid_matrix = [
            [1.0, 4.0, -2.0, 1.0, 1.0],
            [1.0, 2.0, -1.0, 2.0, 0.0],
            [3.0, 1.0, 1.0, 0.0, 0.0],
            [3.0, 1.0, 0.0, 0.0, 0.0],
            [3.0, 0.0, 0.0, 0.0, 0.0]
        ]
        x_values = [1, 1, 2, 2, 2]
        expected = "1.0 + 4.0(x-1) + -2.0(x-1)(x-1) + 1.0(x-1)(x-1)(x-2) + 1.0(x-1)(x-1)(x-2)(x-2)"
        self.assertEqual(expected, generate_polynom_with_brackets(pyramid_matrix, x_values))

    def test_should_return_multipliers_when_second_grade(self):
        pyramid_matrix = [[1.0, 4.0, -2.0], [1.0, 2.0, -1.0], [3.0, 1.0, 1.0]]
        x_values = [1, 1, 2]
        expected = [-5.0, 8.0, -2.0]
        self.assertEqual(expected, generate_multipliers(pyramid_matrix, x_values))

    # def test_should_return_multiplied_out_polynom_when_three_sampling_points(self):
    #     pyramid_matrix = [
    #         [1.0, 4.0, -2.0, 1.0, 1.0],
    #         [1.0, 2.0, -1.0, 2.0, 0.0],
    #         [3.0, 1.0, 1.0, 0.0, 0.0],
    #         [3.0, 1.0, 0.0, 0.0, 0.0],
    #         [3.0, 0.0, 0.0, 0.0, 0.0]
    #     ]
    #     x_values = [1, 1, 2, 2, 2]
    #
    #     polynom_with_brackets = "1.0 + 4.0(x-1) + -2.0(x-1)(x-1) + 1.0(x-1)(x-1)(x-2) + 1.0(x-1)(x-1)(x-2)(x-2)"
    #     expected = "x^4 + -5x^3 + 7x^2 + x + -3"
    #     self.assertEqual(expected, generate_multiplied_out_polynom(pyramid_matrix, x_values))


if __name__ == '__main__':
    unittest.main()
