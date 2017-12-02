a = int(input())
bonus = 0
if a <= 100:
    bonus += 5
    if a % 2 == 0:
        bonus += 1
    elif a % 10 == 5:
        bonus += 2

if a > 100 & a < 1000:
    bonus = a * 2 / 10
    if a % 2 == 0:
        bonus += 1
    elif a % 10 == 5:
        bonus += 2

if a > 1000:
    bonus = a / 10
    if a % 2 == 0:
        bonus += 1
    elif a % 10 == 5:
        bonus += 2

print(bonus)
print(a + bonus)