data = open('9.txt')

count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    if d[0] == d[1] and d[2] == d[3] and d[4] == d[5]:
        count += 1
print(count)