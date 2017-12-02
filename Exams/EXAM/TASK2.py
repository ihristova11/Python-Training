import math
k = int(input())
q = int(input())
c = int(input())
b = int(input())
o = int(input())

norm = q - (c + b)
if norm * o >= k:
    print('YES')
else:
    print('NO ' + '- ' + str(math.ceil(k / norm - o)))