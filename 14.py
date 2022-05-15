s = 9 ** 30 + 3 ** 12 - 27 * 3
count = 0
while s:
    if s % 3 == 2:
        count += 1
    s //=3
print(count)
