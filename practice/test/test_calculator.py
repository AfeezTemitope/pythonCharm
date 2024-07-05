import unittest
from practice.calculator_functions import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_function(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = self.calc.add(-10, -7)
        self.assertEqual(result, -17)

    def test_add_mixed_numbers(self):
        result = self.calc.add(2, -4)
        self.assertEqual(result, -2)

    def test_floating_numbers(self):
        result = self.calc.add(2.2,2.2)
        self.assertEqual(result,4.4)

    def test_float_and_int_numbers(self):
        result = self.calc.add(2.2,2)
        self.assertEqual(result,4.2)

    def test_sstring_of_number(self):
        result = self.calc.add('22','22')
        self.assertEqual(result,44)


if __name__ == '__main__':
    unittest.main()
