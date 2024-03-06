from math import sin, cos
x = 0.3
a = 0.3
b = 0.91
h = 0.05

while a <= x <= b:
    if x < 0.5:
        print("x = ", round(x, 2), "\t", 1 / sin(cos(x * x)))  # cosec(cos(x*x))
        x += h
    elif 0.5 <= x < 0.7:
        print("x = ", round(x, 2), "\t", cos(sin(x)))          # cos(sin(x))
        x += h
    elif x >= 0.7:
        print("x = ", round(x, 2), "\t", sin(1 / cos(x * x)))  # sin(sec(x))
        x += h
