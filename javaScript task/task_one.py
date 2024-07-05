class TaskOne:

    def test_scores(self,result):
        return [detail for detail in result if int(detail) >= 70]


    def scoreUpdate_by_5(self, result):
        return [int(detail) + 5 for detail in result]

    def square_of_each_element(self,result):
        return [int(detail) ** 2 for detail in result]


