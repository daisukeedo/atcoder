N = int(input())
ans = 0

for a in range(1, N):
    #print("a=", a, "(N-1)//a=", (N-1)//a)
    ans += (N-1)//a

print(ans)
