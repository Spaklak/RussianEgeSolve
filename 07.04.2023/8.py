import itertools

s = 'вишня'
count = 0
for i in set(itertools.product(s, repeat=6)):
    d = ''.join(i)
    if d[0] != 'ш' and d[-1] != 'и' and d[-1] != 'я' and d.count('в') <= 1:
        count += 1

print(count)