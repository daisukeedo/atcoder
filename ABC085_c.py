N, Y = map(int, input().split())

# 全検索
for a in range(N+1):
    for b in range(N-a+1):
        c = N-a-b
        if (10000*a+5000*b+1000*c) == Y and (c>=0):
            print(a,b,c)
            #プログラムを終了させるときはexit()
            exit()

print("-1", "-1", "-1")
