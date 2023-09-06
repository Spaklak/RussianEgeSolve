data = open('26_8512.txt')
k = int(data.readline()) # кол-во яиц
n = int(data.readline())
a = []
for i in range(n):
    st,end = map(int, data.readline().split())
    a.append([st,end])

a.sort()
cell = [0] * k
count = 0
last = 0
for i in range(n):
    st = a[i][0]
    end = a[i][1]
    for x in range(k):
        if cell[x] < st:
            count += 1
            cell[x] = end
            last = x + 1
            break

print(last, count)