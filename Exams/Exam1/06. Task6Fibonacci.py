n = int(input())

while n > 0:
    prevF = 1
    currF = 1
    nextF = 2
    while nextF <= n:
        nextF = prevF + currF
        prevF = currF
        currF = nextF
    n -= prevF
    print(prevF)