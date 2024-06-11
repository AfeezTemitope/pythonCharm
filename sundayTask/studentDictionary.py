# student_dictionary = {}
#
# for i in range(2):
#     name = input(f"Enter name of student {i+1}: ")
#     age = int(input(f"Enter age of student {i+1}: "))
#     student_dictionary[name] = age
#     print(student_dictionary)
#
# print()
# print("sorting in alphabetical order")
# sort_by_name = dict(sorted(student_dictionary.items()))
# print(sort_by_name)
# print()
# print("Sorting in alphabetical order")
# sort_by_name = dict(sorted(student_dictionary.items()))
# print(sort_by_name)


def get_and_sort_students():
    student_dictionary = {}
    for i in range(2):
        name = input(f"Enter name of student {i+1}: ")
        age = int(input(f"Enter age of student {i+1}: "))
        student_dictionary[name] = age
    print(student_dictionary)

get_and_sort_students()
