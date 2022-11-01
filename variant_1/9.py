data = open('9.txt')
def checker(a):
    chet = []
    nechet = []
    for i in a:
        if i % 2 == 0:
            chet.append(i)
        elif i % 2 != 0:
            nechet.append(i)
    return sum(nechet) > sum(chet)

count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    if checker(d) == 1:
        count += 1
print(count)