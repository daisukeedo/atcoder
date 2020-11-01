n = int(input())

i = 1
ans = 0
tt = 0
sabun = 0

while i <= n:
    a, b = map(int, input().split())
    if a == 1:
        ans += (b*(b+1))/2
    else:
        sabun = ((a-1))*((a-1)+1)/2
        tt = (b*(b+1))/2-sabun
        ans += tt
    i += 1
    tt = 0
    sabun = 0

print(int(ans))
