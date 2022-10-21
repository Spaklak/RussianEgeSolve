a = []
for i in range(1,1000):
    n = bin(i)[2:]
    if n[-1] == '1':
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    if int(n,2) < 126:
        a.append(int(n,2))
print(max(a))
# 123