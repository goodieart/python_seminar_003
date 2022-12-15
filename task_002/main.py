# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import ceil

user_input = list(map(int, input('Введите числа через пробел: ').split()))
r = user_input.copy()
r.reverse()
center = ceil(len(user_input) / 2)
muls = [a*b for a,b in zip(user_input, r)][:center]

print(f'Результирующий список: {user_input}')
print(f'Произведение пар чисел списка: {muls}')
