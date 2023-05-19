for a in range(1,1000):
    f = True
    for x in range(0,1000):
        for y in range(0,1000):
            f = (x > a) or (y > a) or ((y - 2*x + 12) != 0)
            if f == False:
                break
        if f == False:
            break
    if f:
        print(a)