size = int(input())
time = int(input())


for row in range(0, size - 1):
    if time == 0:
        if row % 2 == 1:
            print('?' * row + '* ' *(size - row - 1) + '*' + '?' * row)
        else:
            print(' ' * row + '* ' * (size - row - 1) + '*' + ' ' * row)
    elif time == size:
        if row % 2 == 1:
            print('?' * row + '- ' *(size - row - 1) + '-' + '?' * row)
        else:
            print(' ' * row + '- ' * (size - row - 1) + '-' + ' ' * row)
    elif row < time:
        if row % 2 == 1:
            print('?' * row + '- ' *(size - row - 1) + '-' + '?' * row)
        else:
            print(' ' * row + '- ' * (size - row - 1) + '-' + ' ' * row)
    elif row > time:
        if row % 2 == 1:
            print('?' * row + '* ' *(size - row - 1) + '*' + '?' * row)
        else:
            print(' ' * row + '* ' * (size - row - 1) + '*' + ' ' * row)



if size % 2 == 0:
    print('?' * (size - 1) + 'o' + '?' * (size - 1))

    for row in range(2, size):
        if time == 0:
            if row % 2 == 0:
                print(' ' * row + '- ' * (size - row - 1) + '-' + ' ' * row)
            else:
                print('?' * (size - row - 1) + '- ' * (size - row - 1) + '-' + '?' * (size - row - 1))
        elif time == size:
            if row % 2 == 1:
                print('?' * row + '- ' * (size - row - 1) + '-' + '?' * row)
            else:
                print(' ' * row + '- ' * (size - row - 1) + '-' + ' ' * row)
        elif row < time:
            if row % 2 == 1:
                print('?' * row + '- ' * (size - row - 1) + '-' + '?' * row)
            else:
                print(' ' * row + '- ' * (size - row - 1) + '-' + ' ' * row)
        elif row > time:
            if row % 2 == 1:
                print('?' * row + '* ' * (size - row - 1) + '*' + '?' * row)
            else:
                print(' ' * row + '* ' * (size - row - 1) + '*' + ' ' * row)
else:
    print(' ' * (size - 1) + 'o' + ' ' * (size - 1))



