for i in range(1,90):
    n = bin(i)[2:]
    for x in range(3):
        if n.count('1') == n.count('0'):
            n += n[-1]
        else:
            if n.count('1') > n.count('0'):
                n += '0'
            else:
                n += '1'
    if int(n,2) % 4 == 0:
        print(i)
#87