a = int(input())
tmp = list(map(int, input().split()))
i=0

while True:
    while i < len(tmp):
        if tmp[i] == max(tmp) and max(tmp) != min(tmp):
            tmp[i] = max(tmp)-min(tmp)
        i+=1

    if max(tmp)==min(tmp):
        print(tmp[0])
        exit()

    i=0