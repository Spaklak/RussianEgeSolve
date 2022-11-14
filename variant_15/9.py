import math

data = open('9.txt')
count = 0
for i in data.readlines():
    spisok = [int(x) for x in i.split()]
    Vmm = math.pi * spisok[0] ** 2 * spisok[1]
    if Vmm > 1000 * 1000:
        count += 1

print(count)