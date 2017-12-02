a = int(input())
#print(a)
for i in range (a):
    if(i == 0 or i == a - 1):
        print ('*' * a)
    else:
        print('*' + " " * (a - 2) + '*')




