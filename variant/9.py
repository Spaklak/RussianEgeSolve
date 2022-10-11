f = open('8.txt')
mainCount = 0
for s in f.readlines():
    d = [int(x) for x in s.split()]
    d.sort()
    if (d[3] < (d[0] + d[1] + d[2])) and (len(d) - len(set(d)) == 1):
        mainCount += 1
print(mainCount)