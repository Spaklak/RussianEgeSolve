import itertools

a = 'БИТКОИН'
count = 0
for i in set(itertools.permutations(a)):
    count += 1
print(count)