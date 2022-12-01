# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import ceil

user_input = list(map(int, input('Введите числа через пробел: ').split()))
muls = []
center = ceil(len(user_input) / 2)

for i in range(center):
    muls.append(user_input[i] * user_input[-i-1])

print(f'Результирующий список: {user_input}')
print(f'Произведение пар чисел списка: {muls}')
