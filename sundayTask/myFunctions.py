class MathOperations:
    def maxOf(self, numbers):
        maximum = None
        for num in numbers:
            if maximum is None or num > maximum:
                maximum = num
        return maximum

    def minOf(self, numbers):
        minimum = None
        for num in numbers:
            if minimum is None or num < minimum:
                minimum = num
        return minimum

    def lengthOf(self, number):
        count = 0
        for _ in number:
            count += 1
        return count

    def sumOf(self, numbers):
        total = 0
        for num in numbers:
            total += num
        return total