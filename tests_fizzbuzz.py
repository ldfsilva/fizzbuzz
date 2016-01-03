import unittest
from fizzbuzz import robot


class FizbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual('1', robot(1))

    def test_say_2_when_2(self):
        self.assertEqual('2', robot(2))

    def test_say_4_when_4(self):
        self.assertEqual('4', robot(4))

    def test_say_fizz_when_3(self):
        self.assertEqual('fizz', robot(3))

    def test_say_fizz_when_6(self):
        self.assertEqual('fizz', robot(6))

    def test_say_fizz_when_9(self):
        self.assertEqual('fizz', robot(9))

    def test_say_buzz_when_5(self):
        self.assertEqual('buzz', robot(5))

    def test_say_buzz_when_25(self):
        self.assertEqual('buzz', robot(25))

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual('fizzbuzz', robot(15))

    def test_say_fizzbuzz_when_30(self):
        self.assertEqual('fizzbuzz', robot(30))

    def test_say_fizzbuzz_when_45(self):
        self.assertEqual('fizzbuzz', robot(45))
