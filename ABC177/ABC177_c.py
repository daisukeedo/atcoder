ans = 0
taikaku = 0

N = int(input())
A = list(map(int, input().split()))

for i in A:
    taikaku += i**2

ans = (sum(A)**2-taikaku)/2
print(int(ans % (10**9+7)))
