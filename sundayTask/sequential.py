numbers = list(range(1, 16))
print("Original list:", numbers)

duplicated_list = numbers + numbers
print("Duplicated list:", duplicated_list)

unique_list = list(set(duplicated_list))
print("Unique list:", unique_list)

def sum_every_third(numbers):
    return sum(numbers[2::3])

print("Sum of every third element:", sum_every_third(unique_list))

def sum_first_middle_last(numbers):
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        middle_elements = (numbers[middle_index - 1] + numbers[middle_index]) / 2
    else:
        middle_elements = numbers[middle_index]
    return numbers[0] + middle_elements + numbers[-1]

print("Sum of first, middle and last elements:", sum_first_middle_last(unique_list))
