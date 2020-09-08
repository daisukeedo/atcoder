import itertools

N = input()
A = map(int, input().split())
cnt = 0

for pair in itertools.combinations(A, 3):
    if (pair[0]!=pair[1]) and (pair[1]!=pair[2]) and (pair[0]!=pair[2]):
        if (pair[0]+pair[1] > pair[2]) and (pair[1]+pair[2] > pair[0]) and (pair[0]+pair[2] > pair[1]):
            cnt += 1

print(cnt)
