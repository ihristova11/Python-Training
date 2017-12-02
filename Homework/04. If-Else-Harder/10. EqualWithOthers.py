import math
n = int(input())
max = 0
sum = 0
for i in range(0,n):
    new = int(input())
    if max < new:
        max = new
    sum += new

if sum == 2 * max:
    print('Yes')
    print('Sum = ' + str(sum - max))

else:
    print('No')
    print('Diff = ' + str(abs(sum - 2 * max)))