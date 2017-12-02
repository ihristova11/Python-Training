import math
n = int(input())
sum1 = 0
sum2 = 0

for i in range(0, n):
    curr1 = int(input())
    sum1 += curr1
for i in range(n, 2 * n):
    curr2 = int(input())
    sum2 += curr2

if sum1 == sum2:
    print('Yes, sum = ' + str(sum1))
else:
    print('No, diff = ' + str(abs(sum1 - sum2)))