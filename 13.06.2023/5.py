a = []
for i in range(1000,10000000):
    n = bin(i)[2:]
    if i % 5 == 0:
        n = n[:3] + n
    else:
        n = n + (bin(i % 3 * 5)[2:])
    r = int(n,2)
    if r > 39000:
        a.append(r)
print(min(a))
