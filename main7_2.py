from random import *
print("Введите количество строк: ")
m = input()
while not(m.isdigit()):
    m = input("Введите количество строк (должно быть положительное число): ")
    if m.isdigit():
        if int(m) < 1:
            continue
m = int(m)

print("Введите количество столбцов")
n = input()
while not(n.isdigit()):
    n = input("Введите количество столбцов (должно быть положительное число): ")
    if n.isdigit():
        if int(n) < 1:
            continue
n = int(n)

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(randint(-10, 10))
    matrix.append(row)
for i in range(m):
    print(matrix[i])

print(' ')

minimalItemColumn = n + 1
minimalItemRow = m + 1
minimalItem = 11
for i in range(m):
    for j in range(n):
        if minimalItem > matrix[i][j]:
            minimalItem = matrix[i][j]
            minimalItemRow = i
            minimalItemColumn = j

for i in range(m):
    del(matrix[i][minimalItemColumn])
del(matrix[minimalItemRow])

for i in range(m - 1):
    print(matrix[i])