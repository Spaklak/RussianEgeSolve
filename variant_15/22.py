f = open('22_1.txt')
procces = [] #список с процессами(столбец B в екселе)
for i in f.readlines():
    procces.append(int(i))#добавляем их в список

f.close()#закрываем первый файл

f2 = open('22_2.txt')
so_procces = []#список с зависимостями(столбец C excel)

for i in f2.readlines():
    i = i.replace('\n','')#убираем символ строки 
    so_procces.append(i.split(';')) #разделяем там где два процесса

f2.close()
mx = 0

for x in range(len(so_procces)):# перебираем список( можно брать и список procces по длине они одинаковы)
    mx = 0
    if len(so_procces[x])==1 and so_procces[x][0]=='0':#если процесс не зависит от какого либо другого, то нам нет смысла его изменять, просто пропускаем
        pass
    else:
        for j in range(len(so_procces[x])):
            if (procces[x]+procces[int(so_procces[x][j])-1])>mx:
                mx = (procces[x]+procces[int(so_procces[x][j])-1])
                
        procces[x] = mx

print(max(procces))#выводим минимальное время через которое завершаться все процессы