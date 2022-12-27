minimal = []
for i in range(1,1000):
    s = ''
    a = i
    while a:
        s += str(a % 3)
        a //= 3
    s = s[::-1]
    s += str(i % 3)
    if len(str(int(s,3))) == 3:
        minimal.append(int(s,3))

print(min(minimal))
