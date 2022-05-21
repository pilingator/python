# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import math
N = int(input('Введите число N (количество эл-тов последвательности))'))
i = 1
result = 0
while i <= N:
    result = math.factorial(i)
    print(f'{i}: {result}')
    i = i + 1