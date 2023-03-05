data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    if d[1] == (2 * d[0] + 3):
        count += 1
print(count)