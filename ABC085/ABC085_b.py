N = int(input())
d=[]
i=0
cnt=0

while i < N:
    i += 1
    d.append(int(input()))

print(len(list(set(d))))

