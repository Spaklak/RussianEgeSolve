data = open('9.txt')
Tol2 = 1e-20
count = 0
for i in data.readlines():
    d = [int(x) for x in i.split()]
    x_1 = d[0]
    y_1 = d[1]
    x_2 = d[2]
    y_2 = d[3]
    x_3 = d[4]
    y_3 = d[5]
    try:
        if ((x_3 - x_1) / (x_2 - x_1) - (y_3 - y_1) / (y_2 - y_1)) ** 2 <= Tol2:
            count += 1
    except ZeroDivisionError:
        pass
print(count)