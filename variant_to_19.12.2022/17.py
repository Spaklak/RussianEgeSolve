data = open('17.txt')
spisok = [int(x) for x in data.read().split()]
countABS = 0
count = 0
maximm = -100000000000000000000000000
for i in spisok:
    if abs(i) < 100:
        countABS += 1

for i in range(len(spisok)-1):
    if (spisok[i] + spisok[i+1]) / 2 > countABS:
        count += 1
        maximm = max(maximm, spisok[i] + spisok[i+1])

print(count, maximm)
