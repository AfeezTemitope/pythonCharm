import unittest
from sundayTask.functionsForThisTask import *


class TestCalculations(unittest.TestCase):
    def test_length(self):
        self.assertEqual(lengthOf([1, 2, 3, 4, 5]), 5)
        self.assertEqual(lengthOf([10, 20, 30]), 3)

    def test_sum(self):
        self.assertEqual(sumOf([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sumOf([10, 20, 30]), 60)

    def test_max(self):
        self.assertEqual(maxOf([1, 2, 3, 4, 5]), 5)
        self.assertEqual(maxOf([10, 20, 30]), 30)

    def test_min(self):
        self.assertEqual(minOf([1, 2, 3, 4, 5]), 1)
        self.assertEqual(minOf([10, 20, 30]), 10)

    def test_even_sum(self):
        self.assertEqual(sumOf([1, 2, 3, 4, 5][1::2]), 6)
        self.assertEqual(sumOf([10, 20, 30, 40, 50][1::2]), 60)

    def test_odd_sum(self):
        self.assertEqual(sumOf([1, 2, 3, 4, 5][::2]), 9)
        self.assertEqual(sumOf([10, 20, 30, 40, 50,25][::2]), 90)


    def test_average(self):
        self.assertEqual(sumOf([1, 2, 3, 4, 5]) / lengthOf([1, 2, 3, 4, 5]), 3)
        self.assertEqual(sumOf([10, 20, 30]) / lengthOf([10, 20, 30]), 20)

    def test_largest(self):
        self.assertEqual(maxOf([1, 2, 3, 4, 5]), 5)
        self.assertEqual(maxOf([10, 20, 30]), 30)

    def test_smallest(self):
        self.assertEqual(minOf([1, 2, 3, 4, 5]), 1)
        self.assertEqual(minOf([10, 20, 30]), 10)

if __name__ == '__main__':
    unittest.main()

