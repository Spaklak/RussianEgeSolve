data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    if d[0] == 0 or d[1] == 0 or d[2] == 0:
        count += 1
    elif sum(d) == 0:
        count += 1
    elif d[0] + d[2] == 0 or d[0] + d[1] == 0 or d[1] + d[2] == 0:
        count += 1

print(count)