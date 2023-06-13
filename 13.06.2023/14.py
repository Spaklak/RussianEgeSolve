for p in range(7,20):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                first = y * p ** 2 + 4 * p ** 1 + y * p ** 0
                second = y * p ** 2 + 6 * p ** 1 + 5 * p ** 0
                third = x * p ** 3 + z * p ** 2 + 3 * p ** 1 + 3 * p ** 0
                if first + second == third:
                    solve = f'{x}{y}{z}'
                    print(int(solve, p))