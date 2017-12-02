age = float(input())
sex = str(input())
sex.lower()
type = ''
if age < 16:
    if sex == 'm' or sex == 'M':
        print('Master')
    elif sex == 'f' or sex == 'F':
        print('Miss')
else:
    if sex == 'm' or sex == 'M':
        print('Mr.')
    elif sex == 'f' or sex == 'F':
        print('Ms.')