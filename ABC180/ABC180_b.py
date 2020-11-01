import math
n = input()
xx = list(map(int, input().split()))
xxx=[]
mht=0
ykr=0
cbs=0

'マンハッタン'
for i in xx:
    mht += abs(i)
    xxx.append(abs(i))
print(mht)

'ユークリッド'
for i in xx:
    ykr += abs(i)**2
print(math.sqrt(ykr))

'チェビシェフ'
print(max(xxx))

