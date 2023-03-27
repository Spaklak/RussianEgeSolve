s = (7 ** (9 ** 2 - 1) - (10 - 3) ** 4 + 453) * 5 * 8 // 6
count = 0
while s:
    if s % 7 == 4:
        count += 1
    s//= 7
print(count)