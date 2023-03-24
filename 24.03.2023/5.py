for i in range(1,1000):
    n = bin(i)[2:]
    for x in range(2):
        n += str(n.count('1') % 2)
    
    if int(n,2) > 64:
        print(i)
        break