for i in range(1,1000):
    p = i
    s = ''
    while p:
        s += str(p%5)
        p//=5
    s = s[::-1]
    if int(s[-1]) % 2 == 0:
        s += '2'
    else:
        s = '2' + s + '3'
    r = int(s,5)
    if r < 1000:
        print(i)