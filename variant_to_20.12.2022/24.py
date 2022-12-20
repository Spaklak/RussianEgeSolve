data = open('24.txt')
spisok = data.read()
count = 1 # 1 2 3 4. Код посчитает 3, а по факту тут 4, поэтому count = 1
listCount = []
for i in range(len(spisok)-1):
    if spisok[i] <= spisok[i+1]:
        count += 1
    else:
        listCount.append(count)
        count = 1

print(max(listCount))
