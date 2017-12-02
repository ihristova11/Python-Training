size = int(input())
time = int(input())

for row in range(0, size):
    if row == size - 1 and row % 2 == 0:
        print('?' * (size -1) + 'o' + '?' * (size - 1))
    if row == size - 1 and row % 2 == 1:
        print(' ' * (size -1) + 'o' + ' ' * (size - 1))
    if time == 0:
        if row % 2 == 0:
            print('* ' * (size - 1) + '*')
        else:
            print('?' * row + '* ' * (size - row - 1) + '*' + '?' * row)
