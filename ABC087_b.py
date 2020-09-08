A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0

#全検索
for a in range(A+1):
    print("a=",a)
    for b in range(B+1):
        print("b=",b)
        for c in range(C+1):
            print("c=",c)
            if 500*a+100*b+50*c == X:
                cnt += 1

print(cnt)
