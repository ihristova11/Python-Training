n = int(input())
type = input()


if n < 100:
    if n >= 20:
        print(0.09 * n)
    else:
        if type == 'day':
            print(0.7 + 0.79 * n)
        elif type == 'night':
            print(0.7 + 0.9 * n)
else:
    print(0.06 * n)