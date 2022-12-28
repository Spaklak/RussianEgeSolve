data = open('17.txt')

spisok = [int(x) for x in data.read().split()]
minim103 = 1000000000000000000000000000000000000
count = 0
maxim = 0
for i in spisok:
    if i % 103 == 0:
        minim103 = min(minim103,i)


for i in range(len(spisok)-1):
    if (spisok[i] + spisok[i+1]) % 2 == 0 and (spisok[i] - spisok[i+1]) % minim103 == 0:
        count += 1 
        maxim = max(maxim, spisok[i] + spisok[i+1])

print(count, maxim)