i = 0
k_n = []
k_n_all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

p_price, k_number = map(int, input().split())
k_n = map(int, input().split())
result_number = list(set(k_n_all) - set(k_n))
result_price = p_price

while True:
    x = 0
    y = 0
    z = list(map(int, str(result_price)))
    while x < len(z):
        if z[x] in result_number:
            y += 0
        else:
            y += 1
        x += 1

    if y == 0:
        print(result_price)
        break
    else:
        result_price += 1
