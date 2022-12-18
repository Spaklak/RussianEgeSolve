for i in range(135790, 163229):
    dels = []
    for x in range(2,int(i**0.5)+1):
        if i % x == 0:
            dels.append(x)
            dels.append(i // x)
    if sum(dels) > 460000:
        print(len(dels), sum(dels))