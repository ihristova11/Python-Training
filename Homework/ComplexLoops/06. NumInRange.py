print('Enter a number in the range [1...100]: ')
n = int(input())

while(n > 100 or n < 1):
    print('Invalid number!')
    print('Enter a number in range [1...100]: ')
    n = int(input())

print('The number is: ' + str(n))