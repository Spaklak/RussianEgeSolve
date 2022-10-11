
data = open('24.txt')
spisok = data.read().split('B')
count = 0
for i in spisok:
    if len(i) == 0:
        pass
    elif i[0] == 'A' and len(i) < 15 and 'F' in i and i.count('A') == 1:
        count += 1

print(count)
#неверно