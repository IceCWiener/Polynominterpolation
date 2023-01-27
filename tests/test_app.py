import unittest
from utility import Utility
from hermite import Hermite
from app import create_polynom


class TestApp(unittest.TestCase):
    def test_should_return_polynom_coefficients_when_second_grade(self):
        util = Utility()
        pyramid_matrix = [[1.0, 4.0, -2.0], [1.0, 2.0, -1.0], [3.0, 1.0, 1.0]]
        x_values = [1, 1, 2]
        expected = [-5.0, 8.0, -2.0]
        self.assertEqual(expected, util.generate_polynom_coefficients(
            pyramid_matrix[0], x_values))

    def test_should_return_multiplied_polynom(self):
        util = Utility()
        pol1 = [1, 5, 2]
        pol2 = [6, 1, 4, 3]
        expected = [6, 31, 21, 25, 23, 6]
        self.assertEqual(expected, util.multiply_polynoms(pol1, pol2))

    def test_should_return_polynom_with_multiplied_elements(self):
        util = Utility()
        pol1 = [1, 5, 2]
        factor = 4
        expected = [4, 20, 8]
        self.assertEqual(
            expected, util.multiply_each_element_of_polynom(pol1, factor))

    def test_should_return_added_polynoms(self):
        util = Utility()
        pol1 = [1, 5, 2]
        pol2 = [6, 1, 18]
        expected = [7, 6, 20]
        self.assertEqual(expected, util.add_polynoms(pol1, pol2))

    def test_should_return_added_polynoms_when_one_empty(self):
        util = Utility()
        pol1 = []
        pol2 = [6, 1, 18]
        self.assertEqual(pol2, util.add_polynoms(pol1, pol2))

    def test_should_return_added_polynoms_when_one_element(self):
        util = Utility()
        pol1 = [1]
        pol2 = [8, 1, 18]
        expected = [9, 1, 18]
        self.assertEqual(expected, util.add_polynoms(pol1, pol2))

    def test_should_return_standard_polynom(self):
        util = Utility()
        coeffiecients = [-3.0, 1.0, 7.0, -5.0, 1.0]
        expected = "p(x) = (1.0)*x^4 + (-5.0)*x^3 + (7.0)*x^2 + (1.0)*x  + (-3.0)"
        self.assertEqual(expected, util.create_string_polynomial(coeffiecients))


    def test_should_return_polynom_when_hermite(self):
        xy_values = [(0, 0), (0, 0), (1, 1), (1, 3)]
        expected = ['Hermite: p(x) = (1.0)*x^3 + \n']
        result = create_polynom(xy_values)
        self.assertEqual(expected, result)

    def test_should_return_polynom_when_Lagrange(self):
        xy_values = [(1, 5), (2, 0), (3, -4)]
        expected = ['Newton: p(x) = (0.5)*x^2 + (-6.5)*x  + (11.0)',
                    'Lagrange: '
                    'L(x) = (3.0) + (-2.5)*x + (0.5)*x^2\n'
                    'L(x) = (-3.0) + (+4.0)*x + (-1.0)*x^2\n'
                    'L(x) = (1.0) + (-1.5)*x + (0.5)*x^2\n'
                    'p(x) = (0.5)*x^2 + (-6.5)*x  + (11.0)\n']
        result = create_polynom(xy_values)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
