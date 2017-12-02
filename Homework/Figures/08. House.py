n = int(input())
for i in range(1, n - (n // 2)):
    if n % 2 == 1:
        print('-' * (n // 2 - i + 1) + '*' * (2 * i - 1) + '-' * (n // 2 - i + 1))
    else:
        print('-' * ((n - (2 * i)) // 2) + '*' * (2 * i) + '-' * ((n - (2 * i)) // 2))
print('*' * n)
for j in range(0, n // 2):
    print('|' + '*' * (n - 2) + '|')