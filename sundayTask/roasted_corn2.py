def count_of_string(count_list):
    count = 0
    for i in count_list:
        if len(i) >= 2 and i[0] == [-1]:
            count += 1
        return count

sequential_list = range(1,15)
