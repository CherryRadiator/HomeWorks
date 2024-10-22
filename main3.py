while True:
    k = 0
    try:
        n = int(input("Введите n (n > 0, целое): "))
        if n < 0:
            print("Неверное значение")
        else:
            while k**2 <= n:
                k += 1
            print(k)
    except ValueError:
        print("Неверное значение")