alreadyCalculatedData = {(1, 0): 1}
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
    if (n, k) in alreadyCalculatedData:
        return alreadyCalculatedData[(n, k)]
    elif k == 0 or k == n:
        alreadyCalculatedData[(n, k)] = 1
        return 1
    elif 0 < k < n:
        result = Combin2(n - 1, k) + Combin2(n - 1, k - 1)
        alreadyCalculatedData[(n, k)] = result
        return result
    if k > n:
        print("Invalid value")
        return 0

#main
while True:
    character = input("To start the program enter 's', to quit enter any other key: ")
    if character == 's':
        n = "n"
        n = isNumber(n)
        k = "k"
        k = isNumber(k)
        print(Combin2(n, k))
    else:
        break