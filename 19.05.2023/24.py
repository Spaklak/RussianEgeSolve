data = open('24.txt').read()
chet = ['2','4']
nechet = ['1','3','5']
s = ''
mainCount = 0
for i in range(len(data)):
    s = data[i]
    count = 0
    for x in range(i+1, len(data)):
        s += data[x]
        if len(s) == 2:
            if s[0] in chet and s[1] in nechet:
                count += 1
                s = ''
            else:
                mainCount = max(count, mainCount)
                s = ''
                break

print(mainCount)