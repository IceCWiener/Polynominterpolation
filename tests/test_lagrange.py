import unittest
from Lagrange_komplett import Lagrange


class TestLagrange(unittest.TestCase):
    def test_should_return_li_function_when_input_n_alle_li_alle_li_x(self):
        lagrange = Lagrange()
        expected = [6.0, -5.0, 1.0, 3.0, -4.0, 1.0, 2.0, -3.0, 1.0]
        n = 3
        x_vlaues = [1, 2, 3]
        Li_function = lagrange.create_li_function(x_vlaues)[0]
        self.assertEqual(expected, Li_function)

    # def test_should_return_polynom_when_input_n_Li_function(self):
    #     lagrange = Lagrange()
    #     expected = [15, -12, 5, 2.5, -3, 4, -1, -4, 6, -2]
    #     n = 3
    #     alle_li_function = [6, -5, 1, 3, -4, 1, 2, -3, 1]
    #     alle_li_x_werte = [1, 2, 3]
    #     Li_function = lagrange.create_Li_function(n, alle_li_function, alle_li_x_werte)
    #     self.assertEqual(expected, Li_function)