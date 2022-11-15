import unittest
from hermite import Hermite


class TestHermite(unittest.TestCase):
    def test_should_return_polynom_when_input_stützstellen(self):
        hermite = Hermite(1, 1, 1, 4, 2, 3)
        expected = "1 + 4.0(x-1)"
        result = hermite.calculate_polynom()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
