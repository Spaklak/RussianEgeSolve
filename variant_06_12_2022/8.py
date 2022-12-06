import itertools
count = 0
for i in set(itertools.permutations('ОДЕКОЛОН')):
    i = ''.join(i)
    if 'ОО' not in i:
        count += 1
print(count)