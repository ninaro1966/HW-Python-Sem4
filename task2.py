# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# Мое решение
# NumberN = int(input('Введите целое число :'))
# i = 2 # первое простое число
# lst = []
# first = NumberN
# while i <= NumberN:
#     if NumberN % i == 0:
#         lst.append(i)
#         NumberN //= i
#         i = 2
#     else:
#         i += 1
# print(f'Простые множител11и числа {first} приведены в списке: {lst}')

# 2 вариант из лекции
# numbers = int(input('Введите число: '))
#
# devlist = []
# dev = 2
# while numbers> 2:
#     if numbers%dev != 0:
#         dev += 1
#     else:
#         numbers //= dev
#         devlist.append(dev)
#
# print(set(devlist))