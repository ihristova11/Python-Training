n = int(input())
if n > 0:
    min = int(input())

for i in range(n - 1):
    current = int(input())
    if min > current:
        min = current

print(min)