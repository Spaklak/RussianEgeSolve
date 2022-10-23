for i in range(1,1000):
    n = bin(i)[2:]
    lastIndex0 = n.rfind('0')
    twoFirst = n[:2]
    n = n[:lastIndex0] + twoFirst + n[lastIndex0+1:]
    n = n[::-1]
    if int(n,2) == 123:
        print(i)
        break
#47