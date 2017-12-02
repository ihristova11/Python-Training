val = float(input())
type = input()
typeEnd = input()
USD = 1.79549
EUR = 1.95583
GBP = 2.53405
if type == 'USD':
    if typeEnd == 'BGN':
        valEnd = val / USD
    if typeEnd == 'EUR':
        valEnd = (val / USD) * EUR
    if typeEnd == 'GBP':
        valEnd = (val / USD) * GBP

if type == 'EUR':
    if typeEnd == 'BGN':
        valEnd = val / EUR
    if typeEnd == 'USD':
        valEnd = (val / EUR) * USD
    if typeEnd == 'GBP':
        valEnd = (val / EUR) * GBP

if type == 'GBP':
    if typeEnd == 'BGN':
        valEnd = val / GBP
    if typeEnd == 'USD':
        valEnd = (val / GBP) * USD
    if typeEnd == 'EUR':
        valEnd = (val / GBP) * EUR

if type == 'BGN':
    if typeEnd == 'GBP':
        valEnd = val / GBP
    if typeEnd == 'USD':
        valEnd = val / USD
    if typeEnd == 'EUR':
        valEnd = val / EUR


print("%6.*f" % (2, valEnd))