for i in range(1,1000):
    n = bin(i)[2:]
    n = n + n[-1]
    if bin(i)[2:].count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if int(n,2) > 105:
        print(int(n,2), i)
        break