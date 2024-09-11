#input = [2, 3, 1, 4, 2, 1]
#output = [6, 7]


def sum_first_three_and_last_three(lst):
    first_three_sum = sum(lst[:3])
    last_three_sum = sum(lst[-3:])
    return first_three_sum, last_three_sum


input = [2, 3, 1, 4, 2, 1]
print(sum_first_three_and_last_three(input))
