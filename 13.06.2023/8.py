import itertools
r = 'ярослав'
sogl = ['р','с','л','в']
glas = ['я', 'о', 'а']
count = 0

for i in set(itertools.permutations(r,5)):
    countGlas = 0
    countSogl = 0
    d = ''.join(i)
    for i in d:
        if i in sogl:
            countSogl += 1
        else: 
            countGlas += 1
    if countSogl > countGlas:
        if 'яо' not in d and 'яа' not in d and 'оя' not in d and 'оа' not in d and 'ая' not in d and 'ао' not in d:
            count += 1

print(count)