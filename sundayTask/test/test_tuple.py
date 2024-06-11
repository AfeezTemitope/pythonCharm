import unittest
from sundayTask.functionsForThisTask import *

class TestTupleOperations(unittest.TestCase):
    def test_odd_sum(self):
        my_tuple = tuple(range(1, 21))
        odd_sum = sumOf(my_tuple[::2])
        self.assertEqual(odd_sum, 100)

    def test_even_sum(self):
        my_tuple = tuple(range(1, 21))
        even_sum = sumOf(my_tuple[1::2])
        self.assertEqual(even_sum, 110)

    def test_smallest_of_my_tuple(self):
        my_tuple = tuple(range(1,21))
        smallest = minOf(my_tuple)
        self.assertEqual(smallest, 1)

    def test_highest_of_my_my_tuple(self):
        my_tuple = tuple(range(1,21))
        highest = maxOf(my_tuple)
        self.assertEqual(highest,20)

    def test_smallest_and_highest_sum(self):
        my_tuple = tuple(range(1, 21))
        smallest = minOf(my_tuple)
        highest = maxOf(my_tuple)
        total = smallest + highest
        self.assertEqual(total, 21)

    def test_unpack_first_five(self):
        my_tuple = tuple(range(1, 21))
        a, b, c, d, e = my_tuple[:5]
        self.assertEqual((a, b, c, d, e), (1, 2, 3, 4, 5))

if __name__ == '__main__':
    unittest.main()
