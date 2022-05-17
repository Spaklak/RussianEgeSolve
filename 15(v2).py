for a in range(1,1000):
    p = 1
    for x in range(1,1000):
        for y in range(1,1000):
            b = ((x + 2 * y) < a) or (y > x) or (x > 20)
            p = p * b
    if p == 1:
        print(a)
