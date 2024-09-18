def even_index(lst):
    new_lst = []
    for item in lst:
        if item % 2 == 0:
            new_lst.append(item)
    return new_lst


input_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_index(input_number))
