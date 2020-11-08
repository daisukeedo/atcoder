n = str(input())
hai = list(map(int, n))
ggk = sum(hai)
cnt = 0
tmpp = 0
tmp = []
zz=0

if ggk % 3 == 0:
    print("0")
    exit()

if ggk < 3:
    print("-1")
    exit()
while zz <= len(hai):
    if ggk % 3 == 1:
        for i in hai:
            if i % 2 == 0:
                tmp = hai.remove(i)
                tmpp = sum(hai)
                if tmpp % 3 == 0:
                    print("1")
                    exit()
    else:
        for i in hai:
            if i % 2 == 0:
                tmp = hai.remove(i)
                tmpp = sum(hai)
                if tmpp % 3 == 0:
                    print("1")
                    exit()
    hai=tmp
    zz+=1

print("-1")
