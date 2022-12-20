'''
99990 9999
'''
data = open('26.txt')
spisok = [int(x) for x in data.read().split()]
spisok.sort()
count = 0
schet = 0
maxim = 0
predLastI = 0
for i in spisok:
    if schet + i <= 99990:
        count += 1
        schet += i
        predLastI = i
    else:
        break

schet = schet - predLastI

for i in spisok:
    if schet + i <= 99990:
        maxim = i

print(count, maxim)
# 1612 и 90