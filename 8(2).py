'''
Разбор решения с помощью itertools
'''

import itertools

s = 'игорь'
count = 0
for i in set(itertools.product(s, repeat=5)): # используется, если у нас не важно кол-во букв. И может быть ииииии
    pass
for i in set(itertools.permutations(s, 4)):# если переставляет буквы в слове( 5 за кол-во букв)
    count += 1
    print(i)
print(count)