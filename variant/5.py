for i in range(1,1000):
    k = i
    i = i - k % 8
    i = i + k % 2
    n = bin(i)[2:]
    for i in range(2):
        n = n + str(n.count('1') % 2)
    if int(n,2) > 97:
        print(int(n,2))
        break