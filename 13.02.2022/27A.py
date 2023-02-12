#280 17 13

data = open('27A.txt')
z = []
for i in data.readlines():
    count = 0
    x = i[:-2]
    if int(i) < 0:
        a = ''
        i = abs(int(i))
        while i:
            if i % 5 == 1:
                count += 1
            i//=5
        if count == 0:
            z.append(x)

print(z)