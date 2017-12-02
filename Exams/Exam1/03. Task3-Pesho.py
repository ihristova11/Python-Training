import math
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
h3 = int(input())
m3 = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())

a1 = h1 * 60 + m1
a2 = h2 * 60 + m2
a3 = h3 * 60 + m3

dur = 1 * 60 + 29

ans = max(p1, p2, p3)
if a1 + dur <= a2:
    ans = max(ans, p1 + p2)
if a2 + dur <= a3:
    ans = max(ans, p2 + p3)
if a3 + dur <= a2:
    ans = max(ans, p3 + p2)
if a3 + dur <= a1:
    ans = max(ans, p1 + p3)
if a2 + dur <= a1:
    ans = max(ans, p2 + p1)
if a1 + dur <= a3:
    ans = max(ans, p1 + p3)

print(ans)