a = 4 ** 625 - 2 * 311 + 2 ** 571 - 48
count = 0
while a:
    if a % 4 == 1:
        count += 1
    a//=4
print(count)