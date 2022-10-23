print('x,y,z,w')
for x in range(2): # 0 1
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((((not(y)) <= w) <= (x <= z)) <= (x <= w)) == 0:
                    print(x,y,z,w, sep='|')