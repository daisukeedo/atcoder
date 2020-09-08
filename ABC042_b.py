str_list = []
i = 1
n_number, l_length = map(int, input().split())
while i <= n_number:
    print(i,"回目")
    w_1 = input()
    str_list.append(w_1)
    i += 1


str_list.sort()
print(''.join(str_list))
