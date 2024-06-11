#1
from functionsForThisTask import *
import random
random.seed(0)
my_list = [random.randint(1,50) for _ in range(10)]
# 3
even_sum = sum(my_list[1::2])

# 4
odd_sum = sum(my_list[::2])

# 5
third_position_multiples = 1
for i in range(2, lengthOf(my_list),3):
    third_position_multiples *= my_list[i]

# 6
average = sum(my_list) / lengthOf(my_list)
# 7
largest = max(my_list)
# 8
smallest = min(my_list)

# print(my_list)
# print(even_sum)
# print(odd_sum)
# print(third_position_multiples)
# print(average)
# print(largest)
# print(smallest)