while True:
    print("Выберите действие. 1 - Минимум из трёх чисел, 2 - Количество цифр в числе, 3 - Сумма чисел от 1 до N, 4 - Факториал")
    action = int(input())
    if action == 1:
        def minimum(a, b, c):
            print("Минимальное число: ", (min(a, b, c)))
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        num3 = int(input("Введите третье число: "))
        minimum(num1, num2, num3)
    if action == 2:
        def quantity(a):
            count = 0
            while a > 0:
                a = a // 10;
                count += 1
            print("Количество цифр числа:", count)
        number = int(input("Введите число для поиска количества цифр: "))
        quantity(number)
    if action == 3:
        def quantity2(a):
            amount = 0
            for i in range(quantityN):
                z = int(input("Введите число: "))
                amount += z
            print("Сумма чисел: ", amount)
        quantityN = int(input("Введите N (сумма чисел от 1 до N): "))
        quantity2(quantityN)
    if action == 4:
        def factorial(a):
            factorial = 1
            while a > 1:
                factorial *= a
                a -= 1
            print("Факториал: ", factorial)
        fac = int(input("Введите число для поиска факториала: "))
        factorial(fac)