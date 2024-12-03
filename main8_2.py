import math

def u(x, y): return x - y
def v(x, y): return x**2 + math.sin(y)
def F(u, v): return math.exp(u-v) + v
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
x = "x"
x = isNumber(x)
y = "y"
y = isNumber(y)
R = math.log(abs(F(u(x, y), v(x, y))) + math.sqrt(u(x, y) * v(x, y)), math.e)
print(R)