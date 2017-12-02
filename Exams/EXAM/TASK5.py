size = int(input())
time = int(input())


if time == 0:
    print('* ' * (size - 1) + '*')
else:
    print('- ' * (size - 1) + '-')
for i in range(2, size):
    if time >= i:
        if i % 2 == 0:
            print('?' * (i - 1) + '- ' + '- ' * (size - i - 1) + '-' + '?' * (i - 1))
        else:
            print(' ' * (i - 1) + '- ' * (size - i + 1) + ' ' * (i - 2))
    else:
        if i % 2 == 0:
            print('?' * (i - 1) + '* ' + '* ' * (size - i - 1) + '*' + '?' * (i - 1))
        else:
            print(' ' * (i - 1) + '* ' * (size - i + 1) + ' ' * ( i - 2))
if size % 2 == 1:
    print(' ' * (size - 1) + 'o' + ' ' * (size - 1))

    for i in range(2, size):
        if time <= size - i:
            if i % 2 == 0:
                print('?' * (size - i) + '- ' * (i - 1) + '-' + '?' * (size - i))
            else:
                print(' ' * (size - i) + '- ' * (i) + ' ' * (size - i - 1))
        else:
            if i % 2 == 0:
                print('?' * (size - i) + '* ' + '* ' * (i - 2) + '*' + '?' * (size - i))
            else:
                print(' ' * (size - i) + '* ' * i + ' ' * (size - i - 1))

else:
    print('?' * (size - 1) + 'o' + '?' * (size - 1))

    for i in range(2, size):
        if time <= size - i:
            if i % 2 != 0:
                print('?' * (size - i) + '- ' * (i - 1) + '-' + '?' * (size - i))
            else:
                print(' ' * (size - i) + '- ' * (i) + ' ' * (size - i - 1))
        else:
            if i % 2 != 0:
                print('?' * (size - i) + '* ' + '* ' * (i - 2) + '*' + '?' * (size - i))
            else:
                print(' ' * (size - i) + '* ' * i + ' ' * (i - 2))

if time == 0:
    print('- ' * (size - 1) + '-')
else:
    print('* ' * (size - 1) + '*')