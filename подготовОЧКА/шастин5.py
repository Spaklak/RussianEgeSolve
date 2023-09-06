for i in range(1,1000):
    n = bin(i)[2:]
    if i % 5 == 0:
        n = n + n[-3:]
    else:
        n = n + (bin(i%5*5)[2:])
    r = int(n,2)
    if r > 256:
        print(i)
        break