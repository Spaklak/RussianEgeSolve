for i in range(4,1000):
    s = '2' + '5' * i
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25','5',1)
        if '355' in s:
            s = s.replace('355','52',1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if s.count('3') == 2:
        print(i)
        break