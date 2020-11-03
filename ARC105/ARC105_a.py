N = list(map(int, input().split()))
if N[0] == N[1]+N[2]+N[3]:
    print("Yes")
    exit()
if N[1] == N[0]+N[2]+N[3]:
    print("Yes")
    exit()
if N[2] == N[0]+N[1]+N[3]:
    print("Yes")
    exit()
if N[3] == N[0]+N[1]+N[2]:
    print("Yes")
    exit()
if N[0]+N[1] == N[2]+N[3]:
    print("Yes")
    exit()
if N[1]+N[2] == N[0]+N[3]:
    print("Yes")
    exit()
if N[2]+N[3] == N[0]+N[1]:
    print("Yes")
    exit()
if N[0]+N[2] == N[1]+N[3]:
    print("Yes")
    exit()

print("No")