data = open('17.txt', 'r')
spisok_main = []
spisok = data.read()
spisok = spisok.split()
for ex in spisok:
    spisok_main.append(int(ex))
count = 0
maximal = []
for i in range(len(spisok_main)-1):
    if (spisok_main[i] + spisok_main[i+1]) % 7 == 0 and (spisok_main[i] * spisok_main[i+1]) % 15 == 0:
        count += 1
        maximal.append(spisok_main[i] + spisok_main[i+1])

print(count, max(maximal))

data.close()