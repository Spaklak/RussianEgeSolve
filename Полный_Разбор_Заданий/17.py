'''
Если вы не смогли сделать задание 16, то это вообще не трогайте.
Тут придётся использовать мозг и знания питона
'''


data = open('17.txt') # открваем файл
spisok = [int(x) for x in data.read().split()] # записываем в нашу переменную список целых чисел из файла 

'''
Всё остальное - это индивидуально делается к каждой задаче. Поэтому не вижу смысла объяснять этот пример
Описания переменных говорит само за себя
'''
spisokEleven = []
countEleven = 0
spisokSeventyn = []
countSeventyn = 0
for i in spisok:
    if i % 11 == 0:
        countEleven += 1
        spisokEleven.append(i)
    if i % 17 == 0:
        countSeventyn += 1
        spisokSeventyn.append(i)

if countEleven > countSeventyn:
    print(countEleven, min(spisokEleven))
else:
    print(countSeventyn, min(spisokSeventyn))

data.close()