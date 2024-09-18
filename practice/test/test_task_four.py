from unittest import TestCase
from just_snacks.task_four import even_index


class Test(TestCase):
    def test_even_index(self):
        input_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = [2, 4, 6, 8, 10]
        index = even_index(input_number)
        self.assertEqual(index, expected_result)

    # def test_for_non_number_value(self):
    #     input_number = ["1", "3", 'dd', 'ytyt']
    #     index = even_index(input_number)
    #     self.assert