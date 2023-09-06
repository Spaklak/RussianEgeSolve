a = []
for x in range(0,15):
    first = 9 * 15 ** 7 + 7 * 15 ** 6 + 9 * 15 ** 5 + 6 * 15 ** 4 + 8 * 15 ** 3 + x * 15 ** 2 + 1 * 15 ** 1 + 3 * 15 ** 0
    second = 7 * 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 1 * 15 ** 1 + 3 * 15 ** 0
    if (first + second) % 11 == 0:
        print(x)
        a.append(x)

print(sum(a))