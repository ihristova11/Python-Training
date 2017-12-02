n = int(input())

s = n * (n + 1) // 2
mod = s % 1000000007

print(pow(mod, 2))