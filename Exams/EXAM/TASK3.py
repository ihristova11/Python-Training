q = int(input())
y = int(input())
x = int(input())

if x > -2 * q and x < 2 * q and y >= -q and y <= q:
    print('INSIDE')
elif (x > -3 * q and x < 3 * q) and ((y > q and y < 2 * q) or (y > -2 * q and y < -q)):
    print('INSIDE')
elif (x == 2 * q or x == -2 * q) and (y >= - q and y <= q):
    print('BORDER')
elif (x > 2 * q and x <= 3 * q) and (y == q or y == -q):
    print('BORDER')
elif (x >= -3 * q and x < -2 * q) and (y == q or y == -q):
    print('BORDER')
elif (x == -3 * q or x == 3 * q) and ((y > q and y <= 2 * q) or y < -q and y >= -2 * q):
    print('BORDER')
elif (y == 2 * q or y == -2 * q) and (x > -3 * q and x < 3 * q):
    print('BORDER')
else:
    print('OUTSIDE')
