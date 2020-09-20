N = int(input())
i=0
cnt = 0
flg = 0

while i < N:
    i += 1
    a, b = map(int, input().split())
    if a == b:
        cnt += 1
        if cnt >= 3:
            flg = 1
    else:
        cnt = 0

if flg == 1:
    print("Yes")
else:
    print("No")