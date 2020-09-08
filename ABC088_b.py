N = int(input())
A = list(map(int, input().split()))
cnt_a = 0
cnt_b = 0
i = 0
new_list = A.sort(reverse=True)

while i < len(A):
    if i % 2 == 0:
        cnt_b += A[i]
    else:
        cnt_a += A[i]
    i += 1

print(cnt_b - cnt_a)
