import math
sec1 = int(input())
sec2 = int(input())
sec3 = int(input())
all = sec1 + sec2 + sec3
min = float(all / 60)
min = math.floor(min)
newSec =  all - min * 60
if newSec < 10:
    print(str(min) + ":0" + str(newSec))
else:
    print(str(min) + ':' + str(newSec))
print(min)
print(newSec)