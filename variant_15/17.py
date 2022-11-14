data = open('17.txt')
spisok = [int(x) for x in data.read().split()]
maxim = 0
count = 0
for i in range(len(spisok)-1):
    raz = spisok[i] - spisok[i+1]
    if abs(raz) % 2 == 0 and abs(raz) % 37 == 0:
        count += 1
        maxim = max(maxim, spisok[i] + spisok[i+1])
print(count,maxim)