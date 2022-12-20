s = 8 ** 1006 + 5 ** 1947 + 505
a = []
while s:
    a.append(s%7)
    s//=7

print(a.count(6)*6 - a.count(2)*2)