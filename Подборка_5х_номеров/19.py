for i in range(96, 1000):
    n = bin(i)[2:]
    for x in range(3):
        if n.count('1') == n.count('0'):
            n += n[-1]
        elif n.count('1') > n.count('0'):
            n += '0'
        else:
            n += '1'
    r = int(n,2)
    if r % 4 == 0:
        print(i)
        break
#103