import itertools
d = 'берсерк'
count = 0
for x in range(5,8):
    for i in itertools.product(d, repeat=x):
        count += 1
print(count)