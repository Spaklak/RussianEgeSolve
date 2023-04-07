print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                p = not((not(x <= (not(w)))) and z)
                l = not(w <= z)
                k = (x <= (not(z)))
                if (p and l and k) == 0:
                    print(x,y,z,w)