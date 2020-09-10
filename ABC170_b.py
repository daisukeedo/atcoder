x, y = map(int, input().split())

a = 2*x-y/2
b = y/2-x
if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
    print("Yes")
else:
    print("No")