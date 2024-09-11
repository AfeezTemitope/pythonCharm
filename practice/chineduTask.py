# def increment_last_element(input_list):
#     for i in input_list:
#         if i[:-1] < 10:
#             input_list[-1] += 1
#             return input_list
#         else:
#             if i[:-1] >= 10:
#                 input_list[i] = str(i)
#                 for i, char in enumerate(input_list):
#                     input_list[i] = str(char)
#                     input_list[i] = str(input_list[i])
#                     input_list[-1] += 1
#                     return input_list
#
#
# input_list = [9, 9, 9, 9]
# output = increment_last_element(input_list)
# print(output)
# #output = [1, 0, 0, 0, 0]

def increment_last_element(input_list):
    for i in range(len(input_list) - 1, -1, -1):
        if input_list[i] < 9:
            input_list[i] += 1
            return input_list
        else:
            input_list[i] = 0
    return [1] + input_list


input_list = [9, 9, 9, 9, 8, 9]
output = increment_last_element(input_list)
print(output)
