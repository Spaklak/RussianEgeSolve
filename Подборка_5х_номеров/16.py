for i in range(1,1000):
    n = bin(i)[2:]
    if n[-1] == '0':
        n = n[:-1] + n[0] + n[1]
        n = n[::-1]
        if int(n,2) == 123:
            print(i)
            break
#54