import unittest
from practice.array_boolean import ArrayBool


class MyTestCase(unittest.TestCase):
    def test_that_arrays_return_actual_value(self):
        arrays = ArrayBool()
        arr = [4, 5, 8, 8, 8, 2, 9]
        result = arrays.badBoy(arr)
        self.assertEqual(result, [False, True, False, False, False, False, True])  # add assertion here


if __name__ == '__main__':
    unittest.main()
