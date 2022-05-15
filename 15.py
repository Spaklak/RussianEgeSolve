def f(x,y,a):
    return ((not(x % a == 0 )) <= ((x % 6 == 0) <= (not(x % 9 ==0))))

for a in range(1,1001):
    fl = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not(f(x,y,a)):
                fl = False
        if fl == False:
            break
    if fl == True:
        print(a)