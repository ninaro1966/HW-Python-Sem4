#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

#Объединенный вариант с репозитория
from random import randint as rI

def createCoef():
    coef = {}
    degree = int(input("Введите максимальную степень: "))
    for i in range(degree, -1, -1):
        coef[i] = rI(-20,20)
    return coef


def createEquation(coefEquation: dict):
    equation = ''
    first = True

    for i in coefEquation.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'

def parseEquation(equation: str):
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    equation = equation.split()
    equation = equation[:-2]

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation

equation1 = createEquation(createCoef())
equation2 = createEquation(createCoef())

parEq1 = parseEquation(equation1)
parEq2 = parseEquation(equation2)

resultEquation ={}
for i in range(max(len(parEq1), len(parEq2)), -1, -1):
    first = parEq1.get(i)
    second = parEq2.get(i)
    if first != None or second != None:
        resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)

def printEquation(equation: str):
    print(equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", ''))

printEquation(createEquation(parEq1))
printEquation(createEquation(parEq2))
printEquation(createEquation(resultEquation))

# Записывала на дискорде - не получилось
# dict1 = {4:-30, 3: 23, 1:45, 0:6}
# dict2 = {6:-5, 5: 3, 4:-30, 3:-23, 2:0, 1:-45, 0:6}
#
# def creatEq(dict):
#     equation = ''
#     first = True
#     for i in range(len(dict),-1, -1):
#         if first:
#             first = False
#             if dict.get(i) and dict.get(i) > 0:
#                 equation += f'{dict.get(i)}x**{i}'
#             if dict.get(i) and dict.get(i) < 0:
#                 equation += f'{dict.get(i)}x**{i}'
#     else:
#         if dict.get(i) > 0:
#             equation += f'{dict.get(i)}x**{i}'
#         if dict.get(i) < 0:
#             equation += f'-{abs(dict.get(i))}x**{i}'
#     return equation
#
# def createDict(equation):
#     equation = equation.replace(' + ', ' +').replace(' - ', ' -').split()
#     finalEq = {}
#     for i in range(len(equation)):
#         finalEq[int(equation[i].split('x**')[1])]=int(equation[i].split('x**')[0])
#     return finalEq
#
# eq1 = creatEq(dict1)
# eq2 = creatEq(dict2)
#
#
# ex1 = createDict(eq1)
# ex2 = createDict(eq2)
#
# def summEq(ex, ex2):
#     finalEquation = {}
#     for i in range(max(len(ex1), len(ex2)), -1, -1):
#         if ex1.get(i) != None or ex2.get(i) != None:
#             finalEquation[i] = (ex1.get(i) if ex1.get(i) else  0) + (ex2.get(i) if ex2.get(i) else  0)
#
#     return finalEquation
#
#
# def printEq(equation):
#     equation = equation.replace('**1', '').replace('x**0', '')
#     print(equation + ' =0')
#
# printEq(creatEq(summEq(ex1, ex2)))
