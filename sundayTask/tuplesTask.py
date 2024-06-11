from functionsForThisTask import *

my_tuple = ()

my_tuple = tuple(range(1, 21))

odd_sum = sumOf(my_tuple[1::2])
print("Sum of elements at odd positions:", odd_sum)

even_sum = sumOf(my_tuple[::2])
print("Sum of elements at even positions:", even_sum)


smallest = minOf(my_tuple)
highest = maxOf(my_tuple)
total = smallest + highest
print("Sum of smallest and highest element:", total)


a, b, c, d, e = my_tuple[:5]
print("First five elements:", a, b, c, d, e)
print(a)








