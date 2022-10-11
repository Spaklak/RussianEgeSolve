for n in range(1,100):
    s = '>' + '0' * 39 + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s :
            s = s.replace('>1', '22>', 1)
        if '>2' in s :
            s = s.replace('>2', '2>', 1)
        if '>0' in s :
            s = s.replace('>0', '1>', 1)
    s = s.replace('>', '')
    a = [int(x) for x in s]
    if sum(a) % 2 != 0:
        print(n, sum(a))