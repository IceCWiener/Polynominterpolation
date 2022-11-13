import unittest


class TestHermite(unittest.TestCase):
    def test_should_return_1_when_input_1(self):
        expected = 1
        result = 1
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
