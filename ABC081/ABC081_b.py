N = int(input())
A = list(map(int, input().split()))
cnt = 0

#リスト内包表記
while all(a % 2 == 0 for a in A):
    #listの中身を全部２で割る
    A = list(map(lambda x: x / 2, A))
    cnt += 1

print(cnt)