f = open('9.txt')
m = []
count = 0
for s in f.readlines():
    d = [int(x) for x in s.split()]
    d.sort()
    if d[3] <= (d[0] + d[1] + d[2]):
        if (d[0] + d[1] == d[2] + d[3]) or (d[0] + d[2] == d[1] + d[3]) or (d[0] + d[3] == d[2] + d[1]):
            count += 1
        elif (d[1] + d[0] == d[2] + d[3]) or (d[1] + d[2] == d[0] + d[3]) or (d[1] + d[3] == d[2] + d[0]):
            count += 1
        elif (d[2] + d[0] == d[1] + d[3]) or (d[2] + d[1] == d[0] + d[3]) or (d[2] + d[3] == d[1] + d[0]):
            count += 1
        elif (d[3] + d[0] == d[1] + d[2]) or (d[3] + d[1] == d[0] + d[2]) or (d[3] + d[2] == d[1] + d[0]):
            count += 1
    else:
        count += 0 
print(count)

# 1 2 3 4