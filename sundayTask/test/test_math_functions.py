import unittest
from sundayTask.myFunctions import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_maxOf(self):
        math_ops = MathOperations()
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(math_ops.maxOf(numbers), 5)

    def test_minOf(self):
        math_ops = MathOperations()
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(math_ops.minOf(numbers), 1)

    def test_lengthOf(self):
        math_ops = MathOperations()
        number = [1, 2, 3, 4, 5]
        self.assertEqual(math_ops.lengthOf(number), 5)

    def test_sumOf(self):
        math_ops = MathOperations()
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(math_ops.sumOf(numbers), 15)

if __name__ == '__main__':
    unittest.main()

