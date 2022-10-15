import math
import functools
from heapq import nlargest
from heapq import nsmallest
from random import randint

while True:
    print("Выберите задание. (1-11)")
    action = int(input())
    #1
    if action == 1:
        print("a: ", (101 + 0) / 3)
        print("b: ", 3.0 * math.e - 6 * 10000000.1)
        print("с: " + str(True & True))
        print("d: " + str(False & True))
        print("e: " + str((False & False) or (True & True)))
        print("f: " + str((False or False) & (True & True)))
    # 2
    if action == 2:
        a2num1 = int(input("Введите первое число:"))
        a2num2 = int(input("Введите второе число:"))
        a2num3 = int(input("Введите третье число:"))
        a2num4 = int(input("Введите четвёртое число:"))
        if a2num1 == a2num2 == a2num3 == a2num4:
            print("Равно.")
        elif a2num1 != a2num2 != a2num3 != a2num4:
            print("Не равно.")
    #3
    if action == 3:
        zad3_list = [randint(-100, 100) for i in range(20)]
        print("Список чисел: ", zad3_list)
        k = int(input("Введите количество наибольших чисел (k): "))
        print("Наибольшие числа: ", nlargest(k, zad3_list))
    #4
    if action == 4:
        zad4_list = [randint(-100, 100) for i in range(20)]
        print("Список чисел: ", zad4_list)
        k = int(input("Введите количество наименьших чисел (k): "))
        print("Наименьшие числа: ", nsmallest(k, zad4_list))
    #5
    if action == 5:
        zad5_list = [randint(-100, 100) for i in range(20)]
        zad5_list2 = []
        print("Список чисел: ", zad5_list)
        a5aver = sum(zad5_list) / len(zad5_list)
        print("Среднее списка: ", a5aver)
        for i in range (20):
            a5num1 = zad5_list.pop()
            if a5aver < a5num1:
                zad5_list2.append(a5num1)
        print("Список чисел больше среднего: ", zad5_list2)
    #6
    if action == 6:
        a6num1 = int(input("Введите первое число:"))
        a6num2 = int(input("Введите второе число:"))
        a6num3 = 0
        for i in range(a6num2):
            a6num3 += a6num1
        print("Результат: ", a6num3)
    #7
    if action == 7:
        zad7_list = [randint(-100, 100) for i in range(20)]
        zad7_listeven = []
        zad7_listodd = []
        print("Список чисел: ", zad7_list)
        for i in range(20):
            a7num1 = zad7_list.pop()
            if a7num1 % 2 == 0:
                zad7_listeven.append(a7num1)
            elif a7num1 % 2 != 0:
                zad7_listodd.append(a7num1)
        print("Список чётных чисел: ", zad7_listeven)
        print("Список нечётных чисел: ", zad7_listodd)

    #8
    if action == 8:
        a8num1 = float(input("Введите температуру в Фаренгейтах: "))
        a8num2 = (a8num1 - 32) / 1.8
        print("Температура в цельсиях: ", a8num2)
    #9
    if action == 9:
        a9num1 = float(input("Введите рост: "))
        a9num2 = int(input("Введите вес: "))
        a9num3 = a9num2 / (a9num1 ** 2)
        print("Индекс массы тела: ", a9num3)
    #10
    if action == 10:
        a10num1 = int(input("Введите число: "))
        print("Вторая степень: ", a10num1 ** 2)
        print("Третья степень: ", a10num1 ** 3)
        print("Четвёртая степень: ", a10num1 ** 4)
    #11
    if action == 11:
        a11num1 = int(input("Введите первое число: "))
        a11num2 = int(input("Введите второе число: "))
        a11num3 = int(input("Введите третье число: "))
        if a11num1 + a11num2 > a11num3 and a11num1 + a11num3 > a11num2 and a11num2 + a11num3 > a11num1:
            print("Заданные длины могут быть треугольником.")
        elif not(a11num1 + a11num2 > a11num3 and a11num1 + a11num3 > a11num2 and a11num2 + a11num3 > a11num1):
            print("Заданные длины не могут быть треугольником.")