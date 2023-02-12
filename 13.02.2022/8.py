from itertools import *

s = 'школа'
count = 0
for i in set(product(s,repeat=3)):
    d = ''.join(i)
    if d.count('к') == 1:
        count +=1

print(count)