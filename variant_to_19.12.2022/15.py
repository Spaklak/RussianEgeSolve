for a in range(1,1000):
    p = 1
    for x in range(1,1000):
        for y in range(1,1000):
            b = (x > 39) or (y > 26) or ( 2 * x + 4 * y < a)
            p *= b
    if p == 1:
        print(a)
        break