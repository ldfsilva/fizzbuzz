"""
Regras do Fizzbuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número.
"""

import unittest
from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(pos):
    message = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        message = 'fizzbuzz'
    elif multiple_of_3(pos):
        message = 'fizz'
    elif multiple_of_5(pos):
        message = 'buzz'

    return message


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


if __name__ == '__main__':
    unittest.main()