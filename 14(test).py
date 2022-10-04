s = 216 ** 1315 - 4 * 36 ** 1502 + 5 * 36 ** 1510 - 3 * 6 ** 1331 - 253
a = []
while s:
    a.append(s % 6)
    s //= 6
a.reverse()
print(a.count(0))