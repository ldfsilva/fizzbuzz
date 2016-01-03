"""
Regras do Fizzbuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número.
"""
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
