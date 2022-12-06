data = open('17.txt','r')
spisok = [int(x) for x in data.read().split()]
count = 0
summa = 100000000000000000000000000000000000
for i in range(len(spisok)-3):
    if spisok[i] > spisok[i+1] > spisok[i+2] > spisok[i+3] and spisok[i] - spisok[i+3] > 1000:
        count += 1
        summa = min(summa, spisok[i]+spisok[i+1]+spisok[i+2]+spisok[i+3])

print(count,summa)