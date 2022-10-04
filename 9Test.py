data = open('9.txt', 'r')
f = data.readlines()
count = 0
for i in f:
    #i.splitlines()
    #i = [int(x) for x in i]
    #i.sort()
    for x in range(3):
        i = i.replace('\t', '')
    print(i)
    #i = [int(x) for x in i]
    #i.sort()
    if int(i[3]) - int(i[0]) >= 50 and int(i[1]) * int(i[2]) <= 1000:
        count += 1
print(count)