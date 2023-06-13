for a in range(1000):
    p = True
    for x in range(1000):
        p = (((x & 52) != 0) and ((x & 36) == 0)) <= (not((x & a) == 0))
        if p == 0:
            break
    if p:
        print(a)
        break