n = int(input())
biggest = int(input())
for i in range(n - 1):
    current = int(input())
    if biggest < current:
        biggest = current

print(biggest)