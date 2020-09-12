N, A, B = map(int, input().split())
cnt = 0
n = 0

while n <= N:
    #数字の各桁数の合計
    result_n = sum(list(map(int, str(n))))
    if A <= result_n <= B:
        cnt = cnt+n
    n += 1

print(cnt)
