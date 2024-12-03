def RectP(x1, y1, x2, y2):
    length = abs(float(x2) - float(x1))
    width = abs(float(y2) - float(y1))
    P = length * 2 + width * 2
    return P

def RectS(x1, y1, x2, y2):
    length = abs(float(x2) - float(x1))
    width = abs(float(y2) - float(y1))
    S = length * width
    return S

def isNumber(variable):
    while True:
        inputtedValue = input("Enter value for variable " + str(variable) + ": ")
        try:
            number = float(inputtedValue)
            return number
        except ValueError:
            print("The value is wrong")
            continue

#main
x1 = "x1"
x1 = isNumber(x1)
y1 = "y1"
y1 = isNumber(y1)
x2 = "x2"
x2 = isNumber(x2)
y2 = "y2"
y2 = isNumber(y2)

print("Perimeter for inputted values: " + str(RectP(x1, y1, x2, y2)))
print("Area for inputted values: " + str(RectS(x1, y1, x2, y2)))