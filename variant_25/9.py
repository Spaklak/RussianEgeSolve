f = open('9.txt')
count = 0
for i in f.readlines():
    d = [int(x) for x in i.split()]
    if ((d[0] + d[1]) / 2) == d[2]:
        count += 1
    elif ((d[0] + d[2]) / 2) == d[1]:
        count += 1
    elif ((d[1] + d[2]) / 2) == d[0]:
        count += 1

print(count)