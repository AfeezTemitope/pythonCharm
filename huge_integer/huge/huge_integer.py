class Huge_integer:
    def __init__(self):
        self.digits = [0] * 40

    def parse(self, s):
        s = s.strip()
        if len(s) > 40:
            raise ValueError("Number exceeds 40 digits")
        for i, char in enumerate(reversed(s)):
            if char.isdigit():
                self.digits[i] = int(char)
            else:
                raise ValueError(f"Invalid character '{char}' in input")

        for i in range(len(s), 40):
            self.digits[i] = 0

    def __str__(self):
        return ''.join(map(str, reversed(self.digits))).lstrip('0') or '0'

    def add(self, other):
        result = Huge_integer()
        carry = 0
        for i in range(40):
            total = self.digits[i] + other.digits[i] + carry
            result.digits[i] = total % 10
            carry = total // 10
        return result

    def subtract(self, other):
        result = Huge_integer()
        borrow = 0
        for i in range(40):
            diff = self.digits[i] - other.digits[i] - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.digits[i] = diff
        return result

    def isEqualTo(self, other):
        return self.digits == other.digits

    def isNotEqualTo(self, other):
        return not self.isEqualTo(other)
