data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    if (d[0] > 90 and d[1] < 90 and d[2] < 90 and sum(d) == 180):
        count += 1
    if (d[1] > 90 and d[0] < 90 and d[2] < 90 and sum(d) == 180):
        count += 1
    if (d[2] > 90 and d[1] < 90 and d[0] < 90 and sum(d) == 180):
        count += 1
print(count)