print("Выберите арифметическое действие. 1 - Сложение, 2 - Вычитание, 3 - Умножение, 4 - Деление, 5 - Квадратное уравнение")
action = int(input())

if action == 5: #Квадратное уравнение
    print("Введите A")
    a = int(input())
    print("Введите B")
    b = int(input())
    print("Введите C")
    c = int(input())
    D = float(b**2-4*a*c) #Получение дискриминанта
    if D < 0:
        print("Нет решений.")
    elif D == 0:
        print("D=0")
        x = float(-1*b/2*a)
        print("x="+str(x))
    elif D > 0:
        print("D="+str(D))
        x1 = float((-1*b+D**2)/(2*a))
        x2 = float((-1*b-D**2)/(2*a))
        print("x1="+str(x1))
        print("x2="+str(x2))
elif action == 1: #Сложение
    print("Введите количество чисел (2 и более)")
    quantity=int(input()) #Количество чисел
    i = 0 #Счётчик
    print("Введите число")
    z = float(input()) #Первое число
    while i < quantity-1:
        print("Введите число")
        y = float(input()) #Последующие числа
        z = z+y
        i += 1 #+Счётчик
    print("Сумма="+str(z))

elif action == 2: #Вычитание
    print("Введите количество чисел (2 и более)")
    quantity=int(input()) #Количество чисел
    i = 0 #Счётчик
    print("Введите число")
    z = float(input()) #Первое число
    while i < quantity-1:
        print("Введите число")
        y = float(input()) #Последующие числа
        z = z-y
        i += 1 #+Счётчик
    print("Разность="+str(z))

elif action == 3: #Умножение
    print("Введите количество чисел (2 и более)")
    quantity=int(input()) #Количество чисел
    i = 0 #Счётчик
    print("Введите число")
    z = float(input()) #Первое число
    while i < quantity-1:
        print("Введите число")
        y = float(input()) #Последующие числа
        z = z*y
        i += 1 #+Счётчик
    print("Произведение="+str(z))

elif action == 4: #Деление
    print("Введите количество чисел (2 и более)")
    quantity=int(input()) #Количество чисел
    i = 0 #Счётчик
    print("Введите число")
    z = float(input()) #Первое число
    while i < quantity-1:
        print("Введите число")
        y = float(input()) #Последующие числа
        z = z/y
        i += 1 #+Счётчик
    print("Частное="+str(z))

