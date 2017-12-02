import math
bunkerX = float(input())
bunkerY = float(input())

n = int(input())

bunkerZdrav = int(input())

ngMin = float(input())
ngMax = float(input())

ccMin = float(input())
ccMax = float(input())

ngBum = 0
ccBum = 0

for i in range(2 * n):
    zalpX = float(input())
    zalpY = float(input())
    if i % 2 == 0:
        if ngMin <= math.sqrt((bunkerX - zalpX) * (bunkerX - zalpX) + (bunkerY - zalpY) * (bunkerY - zalpY)) <= ngMax:
            ngBum += 1
            bunkerZdrav -= 1
            if bunkerZdrav == 0:
                print('NO\nNG')
    else:
        if ccMin <= math.sqrt((bunkerX - zalpX) * (bunkerX - zalpX) + (bunkerY - zalpY) * (bunkerY - zalpY)) <= ccMax:
            ccBum += 1
            bunkerZdrav -= 1
            if bunkerZdrav == 0:
                print('NO\nCC')
if bunkerZdrav > 0:
    print('YES')
    print(ccBum)
    print(ngBum)