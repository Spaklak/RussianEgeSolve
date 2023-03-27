for i in range(200000000, 300000000):
    dels = []
    for x in range(1, int(i ** 0.5) + 1):
        if i % x == 0:
            dels.append(x)
            dels.append(i//x)
    dels.sort()
    dels = set(dels)
    dels = [int(x) for x in dels]
    if len(dels) >= 6:
        m = dels[1] * dels[2] * dels[3] * dels[4] * dels[5]  
        if m < i:
            print(m)