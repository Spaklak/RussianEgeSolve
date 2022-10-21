a = []
for i in range(1, 1000):
    n = ''
    s = []
    while i:
        s.append(i%6)
        i //= 6 
    s = s[::-1]
    for i in s:
        n += str(i)
    n = n + n[-1]
    n = int(n,6)
    n = bin(n)[2:]
    n = n + n[-1]
    n = int(n,2)
    if n < 344:
        a.append(n)
print(max(a))
# 331