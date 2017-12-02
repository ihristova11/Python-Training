import math
n = int(input())
odd = 0
even = 0

for i in range(0, n):
    if i % 2 == 1:
        odd += int(input())
    else:
        even += int(input())


if odd == even:
    print('Yes')
    print('Sum  ' + str(odd))
else:
    print('No')
    print('Diff  ' + str(abs(odd - even)))