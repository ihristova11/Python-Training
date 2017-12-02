n = int(input())
n = n + 1
for i in range(0, n):
    print(' ' * (n - i) + '*' * i + ' | ' + '*' * i )