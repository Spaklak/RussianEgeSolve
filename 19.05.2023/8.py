import itertools

a = 'АМФИБРАХИЙ'
count = 0
for i in set(itertools.permutations(a, 10)):
    d = ''.join(i)
    if d[0:2] == 'АМ' and d[-2:] == 'ИЙ':
        count += 1

print(count)