for a in range(50,121):
    p = True
    for x in range(1,10000):
        p = ((x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0)))
        if p: pass
        else: break
    if p:
        print(a)