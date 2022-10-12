# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# Семинарское решение
from random import randint as rInt

uniqueList = {}
finalStr = ''

listStr = "".join(list(map(str, [rInt(0,9) for i in range(40)])))
print(f'Задана последовательность цифр {listStr}')

for c in listStr:
    if uniqueList.get(c):
        uniqueList[c] = uniqueList.get(c) + 1
    else:
        uniqueList[c] = 1

print(uniqueList)

for i in uniqueList.items():
    if i[1] ==1:
        finalStr += str(i[0])

print(f'Уникальные цифры {finalStr}') if finalStr else print(f'Уникальных позиций нет')



#Свое решение - не совсем то
# myList = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f'Начальный список: {myList}')
# myList2 = []
# [myList2.append(i) for i in myList if i not in myList2]
# print(f"Список встречающихся элементов: {myList2}")