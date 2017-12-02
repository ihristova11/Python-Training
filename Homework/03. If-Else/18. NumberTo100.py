a = int(input())
tens = ''
ones = ''
if a == 100:
    print('one hundred')
else:
    if a <= 20:
        if a == 1:
            print('one')
        elif a == 0:
            print('zero')
        elif a == 2:
            print('two')
        elif a == 3:
            print('three')
        elif a == 4:
            print('four')
        elif a == 5:
            print('five')
        elif a == 6:
            print('six')
        elif a == 7:
            print('seven')
        elif a == 8:
            print('eight')
        elif a == 9:
            print('nine')
        elif a == 10:
            print('ten')
        elif a == 11:
            print('eleven')
        elif a == 12:
            print('twelve')
        elif a == 13:
            print('thirteen')
        elif a == 14:
            print('fourteen')
        elif a == 15:
            print('fifteen')
        elif a == 16:
            print('sixteen')
        elif a == 17:
            print('seventeen')
        elif a == 8:
            print('eighteen')
        elif a == 9:
            print('nineteen')
        elif a == 20:
            print('twenty')

    else:
        b = a % 10
        c = a // 10
        if c == 2:
            tens = 'twenty'
        elif c == 3:
            tens = 'thirty'
        elif c == 4:
            tens = 'forty'
        elif c == 5:
            tens = 'fifty'
        elif c == 6:
            tens = 'sixty'
        elif c == 7:
            tens = 'seventy'
        elif c == 8:
            tens = 'eighty'
        elif c == 9:
            tens = 'ninety'

        if b == 1:
            ones = 'one'
        elif b == 2:
            ones = 'two'
        elif b == 3:
            ones = 'three'
        elif b == 4:
            ones = 'four'
        elif b == 5:
            ones = 'five'
        elif b == 6:
            ones = 'six'
        elif b == 7:
            ones = 'seven'
        elif b == 8:
            ones = 'eight'
        elif b == 9:
            ones = 'nine'

print(str(tens) + ' ' + str(ones))