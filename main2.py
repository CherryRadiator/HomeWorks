from math import *
alfa = (2*pi) / 6
v0_kmPh = 35.0
v0_mPs = v0_kmPh / 3.6
g = 9.81
x = -10.00
y = x * tan(alfa) + (g*x**2)/(2*v0_mPs * cos(alfa)**2)
while y >= 0:
    y = (x * tan(alfa)) + ((g * (x ** 2)) / (2 * (v0_mPs**2) * (cos(alfa) ** 2)))
    print(x, ", ", round(y, 2))
    x += 0.01
print(round(x, 2))