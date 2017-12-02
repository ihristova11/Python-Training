letter = input()
sum = 0
for k in letter:
    if k == 'a' or k == 'A':
        sum += 1
    elif k == 'e' or k == 'E':
        sum += 2
    elif k == 'i' or k == 'I':
        sum += 3
    elif k == 'o' or k == 'O':
        sum += 4
    elif k == 'u' or k == 'U':
        sum += 5
print(sum)