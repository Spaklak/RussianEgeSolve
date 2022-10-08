for i in range(1,1000):
    a = ''
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n += '0'
        a = '10' + n[2:]
    else:
        n += '1'
        a = '11' + n[2:]
    if int(a, 2) > 16:
        print(i)
        break