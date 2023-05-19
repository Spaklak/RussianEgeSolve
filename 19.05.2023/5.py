for i in range(1,1000):
    n = bin(i)[2:]
    n = n[::-1]
    try:
        n = n.replace('0',n[::-1][1]+n[::-1][0],1)
    except:
        continue
    r = int(n,2)
    if r == 119:
        print(i)