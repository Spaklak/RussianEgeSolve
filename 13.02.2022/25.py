from fnmatch import *
a = []
for i in range(3,10**10,10):
    if i ** 2 >= 10 ** 10:
        break
    if fnmatch(str(i**2), '4*1?009'):
        a.append([i,i**2])

for i in range(7,10**10,10):
    if i ** 2 >= 10 ** 10:
        break
    if fnmatch(str(i**2), '4*1?009'):
        a.append([i,i**2])

a.sort()
print(a)