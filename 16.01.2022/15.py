for a in range(1,1000):
    p = True
    for x in range(1,1000):
        p = (160 <= x <= 180) <= ((x % 35 == 0) <= (x % a == 0))
        if p:
            pass
        else:
            break
    if p:
        print(a)