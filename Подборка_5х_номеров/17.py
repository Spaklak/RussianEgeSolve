a = []
for i in range(1,1000):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    if n.count('1') > n.count('0'):
        n += '0'
    else:
        n += '1'
    r = int(n,2)
    if r > 80:
        a.append(r)
print(min(a))
# 81