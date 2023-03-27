for i in range(100,1000):
    n1 = (int(str(i)[0]) ** 2 + int(str(i)[1]) ** 2) 
    n2 = (int(str(i)[1]) ** 2 + int(str(i)[2]) ** 2)
    if n1 > n2:
        n = str(n1) + str(n2)
    elif n2 > n1:
        n = str(n2) + str(n1)
    else:
        n = str(n1) + str(n2)
    if n == '9010':
        print(i)