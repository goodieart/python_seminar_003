# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.(Дополнительно)


def fib(n: int) -> list:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    result = fib(n - 1)
    result.append(result[-1] + result[-2])
    return result

# Здесь напрашивается overload, но python не поддерживает
# перегрузку штатными средствами


def nfib(n: int) -> list:
    if n == -2:
        return [1, -1]
    elif n == -1:
        return [1]

    result = nfib(n + 1)
    result.append(result[-2] - result[-1])
    return result


def generate_seq(value) -> list:
    if value == 0:
        return [0]
    result = nfib(-value)[::-1]
    result.append(0)
    result.extend(fib(value))
    return result


user_input = int(input('Введите число k: '))
print(generate_seq(user_input))
