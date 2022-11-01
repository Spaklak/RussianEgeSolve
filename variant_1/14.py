s = 81 ** 5 + 3 ** 30 - 27
count = 0
while s:
    if s % 9 == 8:
        count += 1
    s//=9
print(count)