data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    if (d[0] + d[4]) ** 2 > d[1] ** 2 + d[2] ** 2 + d[3] ** 2:
        count += 1
print(count)