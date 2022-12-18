for i in range(2,1000):
    n = bin(i)[2:]
    n += n[-2]
    n += n[1]
    if int(n,2) > 100:
        print(i)
        break