def maxDig(n, lastValue=0):
    string = str(n)
    array = string.split('')
    if len(string) == 1:
        return lastValue
    if int(array[0]) > lastValue:
        lastValue = int(array[0])
        return maxDig(n//10, lastValue)

#main
n = input("Введите n: ")
while not(n.isdigit()):
    n = input('Введите n: ')
    if n.isdigit():
        if int(n) > 1:
            n = int(n)
print(maxDig(n))
