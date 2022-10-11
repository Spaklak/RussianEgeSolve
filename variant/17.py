data = open('17.txt')
spisok = [int(x) for x in data.read().split()]
minimum = 100000
count = 0
maxim = []
for i in spisok:
    if i > 0 and i % 19 == 0:
        minimum = min(minimum, i)

for i in range(len(spisok) - 1):
    if spisok[i] + spisok[i+1] < minimum:
        count += 1
        maxim.append(spisok[i] + spisok[i+1])

print(count, abs(max(maxim)))