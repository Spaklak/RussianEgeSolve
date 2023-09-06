for i in range(6,100):
    s = '2' + '4' * i
    while '14' in s or '244' in s or '444' in s:
        if '14' in s:
            s=s.replace('14','2',1)
        if '244' in s:
            s=s.replace('244','14',1)
        if '444' in s:
            s=s.replace('444','21',1)
    
    summa = [int(x) for x in s]
    if sum(summa) > 20:
        print(i)
        break