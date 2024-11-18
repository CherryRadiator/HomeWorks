import random
n = input("Введите количество элементов в списке ")
while not(n.isdigit()):
    n = input("Введите количество элементов в списке ")
    if n.isdigit():
        if int(n) < 0:
            continue
n = int(n)
SomeArray = [random.randint(-20, 20) for i in range(n)]
print(SomeArray)
countNegative = 0
for i in range(n):
    if SomeArray[i] < 0:
        countNegative += 1
print("Количество отрицательных элементов: " + str(countNegative))
minItem = float("inf")
indexOfMinItem = 0
for i in range(n -1 ):
    if (SomeArray[i]**2)**(1/2) < (minItem**2)**(1/2):
        minItem = SomeArray[i]
        indexOfMinItem = i
    else: continue
suma = 0
for i in range(indexOfMinItem, n):
    suma += (SomeArray[i]**2)**(1/2)
print("Сумма всех модулей элементов после минимального модуля: " + str(suma))
