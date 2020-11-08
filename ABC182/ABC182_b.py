from collections import Counter
n = int(input())
aa = list(map(int, input().split()))
yakusu = []

for n in aa:
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i>1:
                yakusu.append(i)
            yakusu.append(n//i)
        i += 1

c = Counter(yakusu)
d = c.most_common()
print(d[0][0])
