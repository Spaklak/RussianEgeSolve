a = []
count = 0
for i in range(1,257):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '11' + n + '0'
    else:
        n = '1' + n + '00'
    n = int(n,2)
    a.append(n)

print(len(a))
print(len(set(a)))