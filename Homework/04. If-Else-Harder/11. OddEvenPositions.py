n = int(input())
even = 0
odd = 0
evenMax = 0
evenMin = 0
oddMax = 0
oddMin = 0
c = 0

if n == 1:
    c = float(input())
    print('OddSum = ' + str(c))
    print('OddMin = ' + str(c))
    print('OddMax = ' + str(c))
    print('EvenSum = 0.0')
    print('EvenMin = No')
    print('EvenMax = No')

elif n == 0:
    c = float(input())
    print('OddSum = 0.0')
    print('OddMin = No')
    print('OddMax = No')
    print('EvenSum = 0.0')
    print('EvenMin = No')
    print('EvenMax = No')
else:
    fodd = float(input())
    feven = float(input())
    oddMax = fodd
    oddMin = fodd
    evenMax = feven
    evenMin = feven
    odd += fodd
    even += feven

    for i in range(0, n - 2):
        if i % 2 == 0:
            c = float(input())
            odd += c
            if oddMax < c:
                oddMax = c
            if oddMin > c:
                oddMin = c

        if i % 2 == 1:
            c = float(input())
            even += c
            if evenMax < c:
                evenMax = c
            if evenMin > c:
                evenMin = c

    print('OddSum = ' + str(odd))
    print('OddMin = ' + str(oddMin))
    print('OddMax = ' + str(oddMax))
    print('EvenSum = ' + str(even))
    print('EvenMin = ' + str(evenMin))
    print('EvenMax = ' + str(evenMax))