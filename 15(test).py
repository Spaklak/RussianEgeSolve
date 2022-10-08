for a in range(1,1000):
    p = 1
    for x in range(1,1000):
        b = ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)
        p = p * b
    if p == 1:
        print(a)
        break