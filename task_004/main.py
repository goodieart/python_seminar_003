# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

from math import modf, ceil


def dec2bin(value: int):
    result = str(value) if value == 0 else ''
    while value != 0:
        value /= 2
        result += str(ceil(modf(value)[0]))
        value = int(value)
    return result[::-1]


user_input = int(input('Введите десятичное число: '))
print(f'Двоичное представление введенного числа: {dec2bin(user_input)}')
