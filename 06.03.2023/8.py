import itertools
count=0
for i in set(itertools.permutations('ИГРОК',5)):
    i = ''.join(i)
    if 'РОК' not in i and i[0] != 'К':
        count += 1
print(count)