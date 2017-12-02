import math
figure = input()
s = 0
if figure == 'triangle':
    a = float(input())
    h = float(input())
    s = a * h / 2
elif figure == 'rectangle':
    b = float(input())
    c = float(input())
    s = b * c
elif figure == 'circle':
    r = float(input())
    s = math.pi * r * r
elif figure == 'square':
    d = float(input())
    s = d * d

print("{0:.3f}".format(s))