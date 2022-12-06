data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    x0 = d[0]
    y0 = d[1]
    x1 = d[2]
    y1 = d[3]
    first = x0 * y0
    second = x1 * y1
    if (first < 0 and second > 0) or (first > 0 and second < 0):
        count += 1

print(count)