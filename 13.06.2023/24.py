data = open('24.txt').read()

chet = ['0','2','4','6','8']
nechet = ['1','3','5','7','9']

for i in chet:
    for x in nechet:
        data = data.replace(i+x, '*')

for i in nechet:
    for x in chet:
        data = data.replace(i+x, '*')

schetCount = []
count = 0
for i in data:
    if i != '*':
        count += 1
    else:
        schetCount.append(count+1)
        count = 1

print(max(schetCount))
