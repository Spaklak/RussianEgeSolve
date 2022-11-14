for a in range(1,1000000000):
    p = 1
    for x in range(1,50):
        for y in range(1,50):
            b = (680 * y + 256 * x < a) or (5 * x + 3 * y > 11111)
            p = p * b
    if p == 1:
        print(a)
        break