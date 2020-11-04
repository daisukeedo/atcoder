import re

n, s = map(str, input().split())
rr = str()
for i in s:
    if i == "A":
        rr += "T"
    if i == "T":
        rr += "A"
    if i == "C":
        rr += "G"
    if i == "G":
        rr += "C"
ans = len(re.findall('AT+', rr))+len(re.findall('TA+', rr))+len(re.findall('GC+', rr))+len(re.findall('CG+', rr))+len(re.findall('ATAT+', rr))+len(re.findall('TATA+', rr))+len(re.findall('CGCG+', rr))+len(re.findall('GCGC+', rr))
print(ans)


# print(re.findall('AT+', rr))
# print(re.findall('TA+', rr))
# print(re.findall('GC+', rr))
# print(re.findall('CG+', rr))
# print(re.findall('ATAT+', rr))
# print(re.findall('TATA+', rr))
# print(re.findall('CGCG+', rr))
# print(re.findall('GCGC+', rr))
