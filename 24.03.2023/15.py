def triangle(a,b,c):
    return (a + b > c) and (a + c > b) and (c + b > a)

for a in range(1,1000):
    p = True
    for x in range(1,1000):
        p = triangle(a,5,x) <= ((max(x,11) <= 19) == (not(triangle(23,13,x))))
        if p == False:
            break
    if p:
        print(a)