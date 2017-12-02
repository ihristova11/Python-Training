n = int(input())


prevF = 1
currF = 1
nextF = 2
for i in range(3, n + 1):
    if i % 2 == 0:
        nextF = currF *  i // 2
        prevF = currF
        currF = nextF
    else:
        nextF = prevF + currF
        prevF = currF
        currF = nextF
print(currF)