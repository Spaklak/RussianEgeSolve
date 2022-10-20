print('x,y,z,w') # вывод x y z w
'''
перебор x y z w в диапазоне от 0 до 1
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(w <= z)) or (x <= y) or (not(x))) == 0: # запись логического выражения
                    print(x,y,z,w, sep='|') # вывод подходящего варианта при котором выражение равно 0 или 1 ( в зависимости от того что указано )