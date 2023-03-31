import itertools
nechet = ['1','3','5','7']
chet = ['0','2','4','6','8']
s = '012345678'
count = 0
for i in (itertools.product(s, repeat = 7)):
    d = ''.join(i)
    if d[0] != '0' and d.count('8') == 1 and d[0] not in nechet and d[-1] not in chet:
        count += 1

print(count)