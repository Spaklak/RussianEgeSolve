for i in range(1,1000):
    k = i - i % 4
    n = bin(k)[2:]
    for k in range(2):
        n += str(n.count('1') % 2)
    if int(n,2) < 64:
        print(i)