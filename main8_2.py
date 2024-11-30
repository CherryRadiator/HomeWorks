def shiftLeft3(a, b, c):
    c1 = a
    b1 = c
    a1 = b
    return [a1, b1, c1]

a1 = input("Введите a1: ")
while not(a1.isdigit()):
    a1 = input("Введите a1: ")
    if a1.isdigit():
        a1 = float(a1)
        continue
b1 = input("Введите b1: ")
while not(b1.isdigit()):
    b1 = input("Введите b1: ")
    if b1.isdigit():
        b1 = float(b1)
        continue
c1 = input("Введите c1: ")
while not(c1.isdigit()):
    c1 = input("Введите c1: ")
    if c1.isdigit():
        c1 = float(c1)
        continue
a2 = input("Введите a2: ")
while not(a2.isdigit()):
    a2 = input("Введите a2: ")
    if a2.isdigit():
        a2 = float(a2)
        continue
b2 = input("Введите b2: ")
while not(b2.isdigit()):
    b2 = input("Введите b2: ")
    if b2.isdigit():
        b2 = float(b2)
        continue
c2 = input("Введите c2: ")
while not(c2.isdigit()):
    c2 = input("Введите c2: ")
    if c2.isdigit():
        c2 = float(c2)
        continue

#main
print(shiftLeft3(a1, b1, c1))
print(shiftLeft3(a2, b2, c2))
