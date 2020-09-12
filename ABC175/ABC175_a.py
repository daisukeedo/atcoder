a = list(str(input()))
cnt=0

if a[0]=="R":
    cnt+=1
    if a[1]=="R":
        cnt+=1
        if a[2]=="R":
            cnt+=1
elif a[1]=="R":
    cnt+=1
    if a[2]=="R":
        cnt+=1
elif a[2]=="R":
    cnt+=1


print(cnt)
