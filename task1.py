# 1. Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# 1. Лучший работающий вариант - из лекции
# import math
# from decimal import Decimal
# d = float(input('Введите шаблон для округления:  '))
#
# def digit_after_dot_counter(num:float):
#     count = 0
#     div = 1
#     while True:
#         if not(num*div == int(num*div)):
#             count += 1
#             div *= 10
#         else: break
#     return count
#
# print(round(math.pi, digit_after_dot_counter(d)))

# 2. Второй работающий вариант
# from decimal import Decimal
# from math import pi#
# d = int(input("Введите число для задания точности числа Пи:\n"))
# print(round(pi, d))

# 3. Теория - Ряд Лейбница
# n = 20000000
#
# mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) + sum(-1/x for x in range(3, n + 1, 4)))
# print(f'{mypi, 100}')