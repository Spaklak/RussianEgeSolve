i = 11
n = bin(i)[2:]
n += n[-2]
n += n[1]
print(n, int(n,2))