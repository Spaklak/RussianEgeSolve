
# ЭТА ЗАЛУПА ЕБАНАЯ  РАБОТАЕТ 
data = open('24.txt').read()
chet = '02468'
nechet = '13579'
countList = []
for i in range(len(data)):
    count = 1
    if data[i] in chet or data[i] in nechet:
        if data[i] in chet:
            for x in range(i+1,len(data)):
                count += 1
                if data[x] in chet or data[x] in nechet:
                    if data[x] in nechet:
                        countList.append(count)
                    break
        if data[i] in nechet:
            for x in range(i+1,len(data)):
                count += 1
                if data[x] in chet or data[x] in nechet:
                    if data[x] in chet:
                        countList.append(count)
                    break

print(max(countList))

countList = []
data = open('24.txt').read()
numbers = ['1','3','5','7','9']
data = data.replace('0','*').replace('2','*').replace('4','*').replace('6','*').replace('8','*')
for i in range(len(data)):
    s = data[i]
    count = 1
    if data[i] in numbers:
        for x in range(i+1,len(data)):
            s += data[x]
            count += 1
            if data[x] == '*':
                countList.append(count)
                if count == 41:
                    print(s)
                break
            if data[x] in numbers:
                break

print(max(countList))

countList = []
data = open('24.txt').read()
numbers = ['0','2','4','6','8']
data = data.replace('1','*').replace('3','*').replace('5','*').replace('7','*').replace('9','*')
for i in range(len(data)):
    s = data[i]
    count = 1
    if data[i] in numbers:
        for x in range(i+1,len(data)):
            s += data[x]
            count += 1
            if data[x] == '*':
                countList.append(count)
                if count == 49:
                    print(s)
                break
            if data[x] in numbers:
                break

print(max(countList))