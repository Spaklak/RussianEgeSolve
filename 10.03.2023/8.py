import itertools
a = 'апельсин'
count = 0
sogl = ['п', 'л', 'с', 'н']
for i in set(itertools.permutations(a,7)):
    d = ''.join(i)
    if 'ь' in d:
        r = d.find('ь')
        try:
            if r-1 == -1:
                continue
            elif d[r-1] in sogl and d[r+1] in sogl:
                count += 1
        except IndexError:
            pass    
    else:
        count += 1

print(count)