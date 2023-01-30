for i in range(1000000, 1500000+1):
    dels = []
    for x in range(2, int(i**0.5)+1):
        if i % x == 0 and ((i // x - x) <= 110):
            dels.append(x)
            dels.append(i//x)
        if len(dels) >= 6:
            break
    if len(dels) >= 6:
        print(i, max(dels))
