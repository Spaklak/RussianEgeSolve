for i in range(1,1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n += '0'
        n = '101' + n[3:]
    else:
        n += '11'
        n = '10' + n[2:]
    if int(n,2) > 68:
        print(i)
        break