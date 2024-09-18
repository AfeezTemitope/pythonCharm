def even_index_sum(lst):
    sum_of_odd = 0
    new_lst = []
    for item in lst:
        if item % 2 != 0:
            sum_of_odd += item
    new_lst.append(sum_of_odd)
    return new_lst


input_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_index_sum(input_number))
