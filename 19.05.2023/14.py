for x in range(0,67):
    first = 1 * 68 ** 4 + 2 * 68 ** 3 + 3 * 68 ** 2 + x * 68 ** 1 + 5 * 68 ** 0
    second = 1 * 68 ** 4 + x * 68 ** 3 + 2 * 68 ** 2 + 3 * 68 ** 1 + 3 * 68 ** 0
    if (second + first) % 12 == 0:
        print((second+first)//12)