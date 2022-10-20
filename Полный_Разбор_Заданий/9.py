f = open('9.txt') # открытие файла
mainCount = 0 # счётчик
for s in f.readlines(): # чтение по строкам
    d = [int(x) for x in s.split()] # занесение в переменную значений ( через запитую, за это отвечает split)
    d.sort() # сортировка списка
    if d[1] - d[0] == d[2] - d[1] and d[1] - d[0] != 0: # наше условие
        mainCount += 1
print(mainCount)