s = 3 * 256 ** 320 - 2 * 64 ** 290 + 4 ** 250 - 1023
massivchik = []
while s:
    massivchik.append(s % 4)
    s //= 4
print(len(massivchik) - massivchik.count(0))