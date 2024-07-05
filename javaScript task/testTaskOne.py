import unittest
from task_one import TaskOne

class MyTestCase(unittest.TestCase):
    #score greater than 70
    def test_that_it_can_filter_score_greater_than_70(self):
        task_one = TaskOne()
        student_score = task_one.test_scores([98,76,65,88,12,45,33,23,45])
        self.assertEqual((student_score), [98,76,88])

    def test_negative_value_for_filter(self):
        task_one = TaskOne()
        student_score = task_one.test_scores([-10,-20,-29])
        self.assertEqual(student_score,[])

    def test_for_string_of_number(self):
        task_one = TaskOne()
        student_score = task_one.test_scores(['22','14'])
        self.assertEqual(student_score,[])

    #score update by 5
    def test_that_5_can_be_added_to_each_score(self):
        task_one = TaskOne()
        student_score = task_one.scoreUpdate_by_5([10,20,30])
        self.assertTrue(student_score,[15,25,35])

    def test_negative_value(self):
        task_one = TaskOne()
        student_score = task_one.scoreUpdate_by_5([-10,-20,-30])
        self.assertEqual(student_score,[-5,-15,-25])

    def test_for_string_of_number(self):
        task_one = TaskOne()
        student_score = task_one.scoreUpdate_by_5(['22','14'])
        self.assertEqual(student_score,[27,19])

    def test_that_each_element_can_be_squared(self):
        task_one = TaskOne()
        student_score = task_one.square_of_each_element([2,4,6])
        self.assertEqual(student_score,[4,16,36])

    def test_that_each_negative_element_can_be_squared(self):
        task_one = TaskOne()
        student_score = task_one.square_of_each_element([-2,-4,-6])
        self.assertEqual(student_score,[4,16,36])

if __name__ == '__main__':
    unittest.main()
