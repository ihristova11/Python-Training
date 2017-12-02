n = int(input())
n = n + 1
for i in range(1, n):
    print(' ' * (n - i) + '* ' * i)
for j in range(1, n ):
    print(' ' * (j + 1) + '* ' * (n - j - 1))