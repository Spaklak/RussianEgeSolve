s = 27 ** 4 - 9 ** 5 + 3 ** 8 - 25
count = 0
while s:
    if s % 3 == 2:
        count += 1
    s //= 3
print(count)