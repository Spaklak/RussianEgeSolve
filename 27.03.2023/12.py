for i in range(301,1000):
    s = '8' * i
    while '555' in s or '888' in s:
        s = s.replace('555','8',1)
        s = s.replace('888','55',1)
    if s == '58' or s == '85':
        print(i)
        break