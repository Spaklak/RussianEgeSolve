count = []
for i in range(9,1000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '1' + n + '00'
    else:
        summa = [int(x) for x in n]
        #n = n + (bin(sum(summa))[2:])
        n = n + bin(n.count('1'))[2:]
    r = int(n,2)
    if r > 88:
        count.append([r,i])

print(min(count))