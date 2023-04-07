for i in range(1,1000):
    n = bin(i)[2:]
    s = n[0]
    for x in n[1:]:
        if x == '0':
            s += '1'
        else:
            s += '0'
    r = int(s,2) + i
    if r > 99 and i % 2 != 0:
        print(i)
        break