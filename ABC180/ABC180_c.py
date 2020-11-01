N = int(input())
i = 1
ans = []
while i*i <= N:
    if N % i == 0:
        ans.append(i)
        ans.append(N//i)
    i += 1

[print(i) for i in sorted(set(ans))]
