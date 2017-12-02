hours = int(input())
minutes = int(input())
mins = 0
hs = 0
if minutes + 15 >= 60:
    hs = hours + 1
    mins = minutes + 15 - 60

else:
    hs = hours
    mins = minutes + 15


if mins < 10:
    mins = '0' + str(mins)
if hs > 23:
    hs = 0

print(str(hs) + ':' + str(mins))