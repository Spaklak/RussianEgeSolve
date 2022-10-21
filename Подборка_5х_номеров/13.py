for i in range(1,1000):
    n = bin(i)[2:]
    s = n[0]
    for x in n[1:]:
        if x == '1':
            s += '0'
        else:
            s += '1'
    s = int(s,2)
    if s + i > 99 and i % 2 != 0:
        print(i)
        break

# 65