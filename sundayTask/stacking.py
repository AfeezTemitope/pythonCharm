def my_len(lst):
    pass


class MyStack:
    def __init__(self):
        self.stack_list =[]
        self.count = 0

    def adding_to_stack(self, item):
        if item != "":
            return self.stack_list.append(item)


    def length(self,word):
        if not word:
            return None
        self.count = 0
        for _ in word:
            self.count += 1
        return self.count

    def pop_it(self):
        if self.length(self.stack_list) > 0:
            last_element = self.stack_list[-1]
            del self.stack_list[-1]
            return last_element
        else:
            return None



