a = []
for i in range(1,1000):
    s = ''
    l = i
    n = []
    while i:
        n.append(i % 3)
        i //= 3
    n = n[::-1]
    for i in n:
        s += str(i)
    s += str(l % 3)
    r = int(s,3)
    if r >= 100: a.append(r)
print(min(a))