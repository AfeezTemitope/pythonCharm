from unittest import TestCase
from small_array import sum_first_three_and_last_three


class Test(TestCase):
    def test_sum_first_three_and_last_three(self):
        input_list = [2, 3, 1, 4, 2, 1]
        result = sum_first_three_and_last_three(input_list)
        expected_result = (6, 7)
        self.assertEqual(result, expected_result)

    def test_negative_list(self):
        input_list = [-1, -3, -2, 9, 0, -1]
        result = sum_first_three_and_last_three(input_list)
        expected_result = (-6, -8)
        self.assertEqual(result, expected_result)
