for i in range(1000000,10000000):
    dels = []
    for x in range(2,int(i**0.5)+1):
        if i % x == 0:
            dels.append(x)
            dels.append(i // x)
    if len(dels) == 1000:
        print(i)
        break