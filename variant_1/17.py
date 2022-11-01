data = open('17.txt')
spisok = [int(x) for x in data.read().split()]
average = sum(spisok) / len(spisok)
count = 0
maxim = 0
for i in range(len(spisok)-2):
    if (spisok[i] > average and spisok[i+1] > average) or (spisok[i] > average and spisok[i+2] > average) or (spisok[i+2] > average and spisok[i+1] > average):
        count += 1
        maxim = max(maxim, spisok[i] + spisok[i+1] + spisok[i+2])
print(count,maxim)
