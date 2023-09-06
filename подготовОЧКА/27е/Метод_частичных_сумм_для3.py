data = open('27B_682.txt')
n = data.readline()
s = [0]
maxim = 0
for i in data.readlines():
    third = [int(x) for x in i.split()]
    summs = []
    for i in range(len(third)):
        for x in range(i+1, len(third)):
            summs.append(third[i] + third[x])
    
    s = [a+b for a in s for b in summs]
    s = {x%4: x for x in (sorted(s))}.values()

for i in s:
    if i % 4 == 0:
        maxim = max(maxim, i)

print(maxim)