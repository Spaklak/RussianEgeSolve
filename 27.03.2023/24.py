data = open('24.txt')
a = []
for i in data.readlines():
    if i.count('A') < 25:
        for x in range(len(i)):
            for j in range(x, len(i)):
                if i[x] == i[j]:
                    a.append(j-x)

print(max(a))