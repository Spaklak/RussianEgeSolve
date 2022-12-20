data = open('17.txt')

spisok = [int(x) for x in data.read().split()]
count = 0
maxim = 0
for i in range(len(spisok)-2):
    if (spisok[i] * spisok[i+1] * spisok[i+2]) % 7 == 0 and abs(spisok[i]+spisok[i+1]+spisok[i+2]) % 10 == 5:
        count += 1
        maxim = max(maxim,spisok[i]+spisok[i+1]+spisok[i+2])

print(count, maxim)
#153 19285