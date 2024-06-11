def maxOf(numbers):
    maximum = None
    for num in numbers:
        if maximum is None or num > maximum:
            maximum = num
    return maximum

def minOf(numbers):
    minimum = None
    for num in numbers:
        if minimum is None or num < minimum:
            minimum = num
    return minimum

def lengthOf(number):
    count = 0
    for _ in number:
        count += 1
    return count

def sumOf(numbers):
    total = 0
    for num in numbers:
        total += num
    return total



