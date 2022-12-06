s = 5 * 36 ** 7 + 6 ** 10 - 36
count = 0
while s:
    if s % 6 == 5:
        count += 1
    s//=6
print(count)