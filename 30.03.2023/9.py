data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    if d[3] ** 3 >= 2 * d[1] * d[0] * d[2] and d[0] > 10 and d[1] > 10 and d[2] > 10 and d[3] > 10:
        count += 1

print(count)