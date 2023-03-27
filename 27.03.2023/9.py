data = open('9.txt', 'r')
conut = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    if d[0] * d[3] >= d[1] * d[2]:
        conut += 1

print(conut)