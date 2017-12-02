w = float(input())
h = float(input())

h *= 100
w *= 100

h -= 100
place = 70 * 120

print((h // 70) * (w // 120 ) - 3)