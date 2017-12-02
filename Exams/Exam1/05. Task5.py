n = int(input())
m = int(input())
q = int(input())

print('|' + '-' * (2 * n + 1) + '|')
for k in range(1, q // n + 1):
    print('|.' + 'X.' * n + '|')
if q % n == 0:
    for j in range (q // n + 1, m + 1):
        print('|.' + 'O.' * n + '|')
else:
    print('|.' + 'X.' * (q % n) + 'O.' * (n - q % n) + '|')
    for l in range(q // n + 2, m + 1):
        print('|.' + 'O.' * n + '|')

print('|' + '-' * (2 * n + 1) + '|')
print('v' + ' ' * (2 * n + 1) + 'v')