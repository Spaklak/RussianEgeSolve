maxim = 0
for i in range(9,10000):
    n = i
    n = n - (n % 8)
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n += '00'
    else:
        n += '01'
    if int(n,2) < 353:
        #maxim = max(maxim, i)
        print(i)