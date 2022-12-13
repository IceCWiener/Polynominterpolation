import unittest
from Lagrange_komplett import Lagrange
from utility import Utility


class TestHermite(unittest.TestCase):
    def test_should_return_li_function_when_input_n_alle_li_alle_li_x(self):
        lagrange = Lagrange()
        expected = [3, 2.5, 0.5]
        n = 3
        alle_li_function = [6, -5, 1]
        alle_li_x_werte = [2]
        Li_function = lagrange.create_Li_function(n, alle_li_function, alle_li_x_werte)
        self.assertEqual(expected, Li_function)