import math
i = 1
z = 0
t = 0
n, d = map(int, input().split())
while i <= n:
    i += 1
    a, b = map(int, input().split())
    if math.sqrt(a**2 + b**2) <= d:
        t += 1

print(t)
