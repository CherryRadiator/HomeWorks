def isNumber(variable):
    while True:
        inputtedValue = input("Enter value for variable " + str(variable) + ": ")
        try:
            number = int(inputtedValue)
            return number
        except ValueError:
            print("The value is wrong")
            continue
def Combin2(n, k):
    if k == 0 or k == n:
        return 1
    elif 0 < k < n:
        return Combin2(n - 1, k) + Combin2(n - 1, k - 1)

#main
n = "n"
n = isNumber(n)
k = "k"
k = isNumber(k)
print(Combin2(n, k))
