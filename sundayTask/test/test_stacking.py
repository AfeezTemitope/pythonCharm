import unittest
from sundayTask.stacking import MyStack


class MyTestCase(unittest.TestCase):
    def test_that_stack_can_add(self):
        stack = MyStack()
        stack.adding_to_stack("my nanme is afeez")
        stack.adding_to_stack("bad afeez is not actually bad")
        stack.adding_to_stack("python seems sexy tho")
        self.assertEqual(stack.length(stack.stack_list),3)

    def test_string_length_with_empty_list(self):
        stack = MyStack()
        self.assertEqual(stack.length([]), None)

    def test_empty_string(self):
        stack = MyStack()
        self.assertEqual(stack.length(""), None)

    def test_that_it_is_empty_and_it_can_add(self):
        stack = MyStack()
        self.assertEqual(stack.length([]), None)
        stack.adding_to_stack("bad afeez")

        self.assertEqual(stack.length(stack.stack_list), 1)

    def test_that_it_can_remove(self):
        stack = MyStack()
        stack.adding_to_stack("tomi")
        stack.adding_to_stack("badAffez")
        self.assertEqual(stack.length(stack.stack_list),2)
        stack.pop_it()
        self.assertEqual(stack.length(stack.stack_list),1)

    def test_that_it_can_remove_and_check_the_last_removed(self):
        stack = MyStack()
        stack.adding_to_stack("tomi")
        stack.adding_to_stack("badAffez")
        self.assertEqual(stack.length(stack.stack_list), 2)
        popped_element = stack.pop_it()
        self.assertEqual(popped_element, "badAffez")
        self.assertEqual(stack.length(stack.stack_list), 1)




if __name__ == '__main__':
    unittest.main()
