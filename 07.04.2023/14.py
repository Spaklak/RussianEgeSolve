s = 7 * 512 ** 1912 + 6 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022
count = 0
while s:
    if s % 8 == 7:
        count += 1
    s//= 8
print(count)