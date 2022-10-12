import functools
import math
while True:
    print(
        "Выберите арифметическое действие. 1 - Сложение, 2 - Вычитание, 3 - Умножение, 4 - Деление, 5 - Квадратное уравнение")
    action = int(input())
    if action == 5:
        entered_list = input("Введите a b c через пробел: ").split()
        num_list = list(map(float, entered_list))
        D = num_list[1] ** 2 - 4 * num_list[0] * num_list[2]
        if D < 0:
            print("Нет решений.")
        if D == 0:
            print("D=0")
            x = float(-1 * num_list[1] / 2 * num_list[0])
            print("x=" + str(x))
        if D > 0:
            print("D=" + str(D))
            x1 = float((-1 * num_list[1] + math.sqrt(D)) / (2 * num_list[0]))
            x2 = float((-1 * num_list[1] - math.sqrt(D)) / (2 * num_list[0]))
            print("x1=" + str(x1))
            print("x2=" + str(x2))
    elif action:
        entered_list = input("Введите список чисел, разделенных пробелом: ").split()
        num_list = list(map(int, entered_list))
        print("Список чисел: ", num_list)
        if action == 1:
            print("Сумма списка:", functools.reduce(lambda x, y: x + y, num_list))
        if action == 2:
            print("Разность списка:", functools.reduce(lambda x, y: x - y, num_list))
        if action == 3:
            print("Произведение списка:", functools.reduce(lambda x, y: x * y, num_list))
        if action == 4:
            print("Частное списка:", functools.reduce(lambda x, y: x / y, num_list))