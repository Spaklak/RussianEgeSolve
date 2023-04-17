data = open('9.txt')
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    d.sort()
    listCount3 = []
    for i in d:
        if i % 3 == 0:
            listCount3.append(i)
    if len(listCount3) == 3:
        if max(d) - min(d) <= sum(listCount3):
            count += 1
print(count)