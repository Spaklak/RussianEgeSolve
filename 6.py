for i in range(1,1000):
    s = i
    n = 600
    while s > 0:
        n //= 3
        s //= 6
    if n == 22:
        print(i)
        break