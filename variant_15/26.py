data = open('26.txt')
cinema = {

}
for i in data.readlines():
    d = [int(x) for x in i.split()]
    ryad = d[0]
    number = d[1]
    if ryad in cinema:
        cinema[ryad].append(number)
    else:
        cinema[ryad] = [number]
listcount = []
count = 0
maxim = 0
maximkeys = 0
for keys in cinema:
    spisokForrange = sorted(cinema[keys])
    listcount = []
    count = 0
    for i in range(len(spisokForrange)):
        try:
            if abs(spisokForrange[i] - spisokForrange[i+1]) == 1:
                count += 1
            else:
                count += 1
                listcount.append(count)
                count = 0
        except:
            count += 1
            listcount.append(count)
    if max(listcount) >= maxim:
        if keys > maximkeys:
            maxim = max(listcount)
            maximkeys = keys
print(maximkeys, maxim)