for i in range(10000000,20000000):
    dels = []
    for x in range(2,int(i**0.5)+1):
        if i % x == 0:
            dels.append(x)
            dels.append(i // x)
    if len(dels) < 3:
        continue
    else:
        dels.sort()
        if (dels[-1] + dels[-2] + dels[-3]) ** 0.5 == int((dels[-1] + dels[-2] + dels[-3]) ** 0.5):
            print(dels[-1] + dels[-2] + dels[-3])