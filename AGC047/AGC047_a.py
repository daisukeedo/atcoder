import itertools
from decimal import Decimal

number_set = list()
i = 1
u = 0
y = 0

a = int(input())
while i <= a:
    number_set.append(Decimal(input()))
    i += 1

for pair in itertools.combinations(number_set, 2):
    if (pair[0] * pair[1])-int((pair[0] * pair[1])) == 0:
        u += 1

print(u)