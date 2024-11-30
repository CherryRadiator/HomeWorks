from math import *

def functionHelper(a, b):
    return sqrt(a**2 + b**2 + sin(a*b)**2)

#main
x = input("Введите x: ")
while (not(x.isdigit())):
    x = input("Введите x: ")
    if x.isdigit():
        x = float(x)
        continue
y = input("Введите y: ")
while (not(y.isdigit())):
    y = input("Введите y: ")
    if y.isdigit():
        y = float(y)
        continue
z = input("Введите z: ")
while (not(z.isdigit())):
    z = input("Введите z: ")
    if z.isdigit():
        z = float(z)
        continue

s = functionHelper(x, y) + functionHelper(x, z) + functionHelper(y, z)
print("Результат: " + str(s))