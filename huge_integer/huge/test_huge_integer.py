from unittest import TestCase
from huge.huge_integer import Huge_integer


class TestHuge_integer(TestCase):
    def test_parse(self):
        h = Huge_integer()
        h.parse("1234567890123456789012345678901234567890")
        self.assertEqual(str(h), "1234567890123456789012345678901234567890")

    def test_that_only_string_of_number_can_be_subtracted(self):
        h1 = Huge_integer()
        h2 = Huge_integer()
        h1.parse("90")
        h2.parse("10")
        result = h1.subtract(h2)
        self.assertEqual(str(result), "80")

    def test_that_string_of_negative_number_can_be_subtracted(self):
        h1 = Huge_integer()
        h2 = Huge_integer()
        h1.parse("-1")
        h2.parse("-2")
        result = h1.subtract(h2)
        self.assertEqual(str(result), "-1")




