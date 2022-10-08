data = open('17.txt')
sl = data.read()
spisok = [int(x) for x in sl.split()]
count = 0
minimum = min(spisok)
maxim = 0
for i in range(0, len(spisok) - 1):
    if spisok[i] % 117 == minimum or spisok[i+1] % 117 == minimum:
        count += 1
        maxim = max(maxim, spisok[i] + spisok[i+1])

print(count,maxim)