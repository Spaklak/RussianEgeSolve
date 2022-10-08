from itertools import product
data = open('1.txt', 'w')
a = '01234567'
count = 0
for i in product(a, repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('6') == 1 and '61' not in s and '16' not in s and '63' not in s and '36' not in s and '65' not in s and '56' not in s and '67' not in s and '76' not in s:
        count += 1
        data.write(s + '\n')
print(count)
data.close()