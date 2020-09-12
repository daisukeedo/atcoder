N = int(input())
A = list(map(int, input().split()))
sa = 0
i = 0

while i < len(A)-1:
    if A[i] > A[i+1]:
        sa += A[i]-A[i+1]
        A[i+1] = A[i]
    i += 1

print(sa)
