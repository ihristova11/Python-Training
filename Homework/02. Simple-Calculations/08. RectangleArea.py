import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
area = math.fabs(x1 - x2) * math.fabs(y1 - y2)
perimeter = 2 * (math.fabs(x1 - x2) + math.fabs(y1 - y2))
print(area)
print(perimeter)