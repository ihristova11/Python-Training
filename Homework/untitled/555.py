size = int(input())
time = int(input())

for i in range(1, size):
    if time == 0:
        if i % 2 == 0:
            print('?' * (i - 1) + '* ' * (size - i) + '*' + '?' * (i - 1))
        else:
            print(' ' * (i - 1) + '* ' * (size - i) + '*' + ' ' * (i - 1))
    elif time == size - 1:
        if i % 2 == 0:
            print('?' * (i - 1) + '- ' * (size - i) + '-' + '?' * (i - 1))
        else:
            print(' ' * (i - 1) + '- ' * (size - i) + '-' + ' ' * (i - 1))
    else:
        if time >= i:
            if i % 2 == 0:
                print('?' * (i - 1) + '- ' * (size - i) + '-' + '?' * (i - 1))
            else:
                print(' ' * (i - 1) + '- ' * (size - i) + '-' + ' ' * (i - 1))
        else:
            if i % 2 == 0:
                print('?' * (i - 1) + '* ' * (size - i) + '*' + '?' * (i - 1))
            else:
                print(' ' * (i - 1) + '* ' * (size - i) + '*' + ' ' * (i - 1))
if size % 2 == 0:
    print('?' * (size - 1) + 'o' + '?' * (size - 1))
else:
    print(' ' * (size - 1) + 'o' + ' ' * (size - 1))

for j in range(size + 1, 2 * size):
    if time == 0:
        if j % 2 == 0:
            print('?' * (2 * size - j - 1) + '- ' * (j - size) + '-' + '?' * (2 * size - j - 1))
        else:
            print(' ' * (2 * size - j - 1) + '- ' * (j - size) + '-' + ' ' * (2 * size - j - 1))
    elif time == size - 1:
        if j % 2 == 0:
            print('?' * (2 * size - j - 1) + '* ' * (j - size) + '*' + '?' * (2 * size - j - 1))
        else:
            print(' ' * (2 * size - j - 1) + '* ' * (j - size) + '*' + ' ' * (2 * size - j - 1))
    else:
        if j < 2 * size - time:
            if j % 2 == 0:
                print('?' * (2 * size - j - 1) + '- ' * (j - size) + '-' + '?' * (2 * size - j - 1))
            else:
                print(' ' * (2 * size - j - 1) + '- ' * (j - size) + '-' + ' ' * (2 * size - j - 1))
        else:
            if j % 2 == 0:
                print('?' * (2 * size - j - 1) + '* ' * (j - size) + '*' + '?' * (2 * size - j - 1))
            else:
                print(' ' * (2 * size - j - 1) + '* ' * (j - size) + '*' + ' ' * (2 * size - j - 1))