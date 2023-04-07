data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    if len(d) - len(set(d)) == 1 and d[3] < d[0] + d[1] + d[2]:
        count += 1
print(count)