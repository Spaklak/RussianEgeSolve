for i in range(1204300, 1204380):
    dels = []
    for x in range(2,int(i**0.5)+1):
        if i % x == 0:
            if x % 2 == 0:
                dels.append(x)
            if (i//x) % 2 == 0:
                dels.append(i // x)
    s = sum(dels)
    if s > 0 and s % 10 == 0:
        print(i,s)