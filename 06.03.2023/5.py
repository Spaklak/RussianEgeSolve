for i in range(1,1000):
    n = bin(i)[2:]
    n += n[-1]
    if str(i)[2:].count('1') % 2 == 0: n += '0'
    else: n += '1'
    n += '0'
    if int(n,2) > 90:
        print(i)
        break