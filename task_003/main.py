# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from math import modf

user_input = list(
    map(float, input('Введите вещественные числа через пробел: ').split()))
fractions = list(map(lambda x: modf(x)[0], user_input))

result = round(max(fractions) - min(fractions), 4)

print(
    f'Разница между max и min значениями дробной части элементов равна {result}')
