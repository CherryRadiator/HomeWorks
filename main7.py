from random import *
print("Введите размер матрицы ")
n = input()
while not(n.isdigit()):
    n = input("Введите количество элементов в списке (должно быть положительным числом) ")
    if n.isdigit():
        if int(n) < 1:
            continue
n = int(n)

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(-10, 10))
    matrix.append(row)

for i in range(n):
    print(matrix[i])

summa = 0
for i in range(n):
    for j in range(i, n - 1):
        summa += matrix[i][j + 1]
print(summa)