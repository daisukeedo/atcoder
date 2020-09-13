import itertools

s = int(input())
n = 1

S = []
ans = []

while n <= s:
    a, b = map(int, input().split())
    S.append([a, b])
    n += 1

for pair in itertools.combinations(S, 2):
    ans.append(abs(pair[0][0] - pair[1][0])+abs(pair[0][1] - pair[1][1]))

print(max(ans))
