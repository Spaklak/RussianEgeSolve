for x in range(0,14):
    first = 7 * 13 ** 4 + 5 * 13 ** 3 + 3 * 13 ** 2 + x * 13 ** 1 + 2 * 13 ** 0
    second = 2 * 13 ** 4 + x * 13 ** 3 + 1 * 13 ** 2 + 7 * 13 ** 1 + 3 * 13 ** 0
    if (first + second) % 12 == 0:
        print(x, (first + second) / 12)