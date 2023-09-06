data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    if (len(d) == len(set(d)) and (not(2*(d[0]+d[4]) < (d[1]+d[2]+d[3])))):
        count += 1
    elif (len(d) != len(set(d)) and ((2*(d[0]+d[4]) < (d[1]+d[2]+d[3])))):
        count += 1
    

print(count)