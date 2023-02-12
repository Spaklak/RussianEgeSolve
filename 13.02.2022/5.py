a = []
for i in range(20,600+1):
    n = bin(i)[2:]
    n = n[:-2]
    a.append(int(n,2))

print(len(set(a)))