#数値の入力
a = int(input())

#文字列の入力
a = str(input())

#文字列の入力をlist
a = list(str(input()))

#スペース区切りの数値の入力をmap
a = map(int, input().split())

#スペース区切りの文字の入力をmap
a = map(str, input().split())

#mapをforで回す
for i in a:

#スペース区切りの数値をlistに入れて合計
N = sum(list(map(int, input().split())))

#２つの配列のそれぞれの要素の比較
for ss, tt in zip(S, T):

#文字列置換
s = s.replace('eraser', '')

#リスト内包表記
while all(a % 2 == 0 for a in A):

#プログラムを終了させるときはexit()
exit()

#ブロックを出るときはbreak
break

#全検索
for a in range(A+1):
    print("a=",a)
    for b in range(B+1):
        print("b=",b)
        for c in range(C+1):
            print("c=",c)
            if 500*a+100*b+50*c == X:
                cnt += 1