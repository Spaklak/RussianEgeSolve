
data = open('9.txt')
count = 0

for i in data.readlines():
    d = [int(x) for x in i.split()]
    if d[0] != min(d) and d[3] != max(d) and d[3] != min(d) and d[0] != max(d):
        d.sort()
        try:
            if (max(d) - min(d)) % (d[1] - d[2]) == 0:
                count += 1
        except ZeroDivisionError:
            count += 0

print(count)