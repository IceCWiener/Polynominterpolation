import unittest
from lagrange import Lagrange


class TestLagrange(unittest.TestCase):
    def test_should_return_li_function_when_input_n_alle_li_alle_li_x(self):
        lagrange = Lagrange()
        expected = [6.0, -5.0, 1.0, 3.0, -4.0, 1.0, 2.0, -3.0, 1.0]
        n = 3
        x_vlaues = [1, 2, 3]
        Li_function = lagrange.create_li_function(x_vlaues)[0]
        self.assertEqual(expected, Li_function)