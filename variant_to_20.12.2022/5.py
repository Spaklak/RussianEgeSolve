for i in range(0,110):
    n = bin(i)[2:]
    if len(n) < 8:
        while len(n) != 8:
            n = '0' + n
    n = n[0:2] + n[6:8]
    if int(n,2) == 7:
        print(i)