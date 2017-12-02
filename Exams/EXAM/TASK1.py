n = int(input())
k = int(input())

num = (pow(5, n) * pow(2, k)) / (pow(5, k // n) * pow(2, n % k))
print('{0:.10f}'.format(num))