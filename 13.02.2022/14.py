a = []
s= 51 * 7 ** 12 - 7 ** 3 - 22
while s > 0:
    a.append(s%7)
    s//=7
print(sum(a))