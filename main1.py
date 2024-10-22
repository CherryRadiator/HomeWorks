s = 10.0
k = 1
while True:
    try:
        P = float(input("на сколько процентов увеличивал лыжник длину пробега каждый день(от 0 до 50)?: "))
        if P >= 50 or P <= 0:
            print("значение выходит за рамки")
        else:
            while (s <= 200):
                s = s + s*P*0.01
                k += 1
            print("Суммарное количество дней:" + str(k))
            print("Количество пробега за " + str(k) + " дней: " + str(s))
            break
    except ValueError:
        print("Введите число")