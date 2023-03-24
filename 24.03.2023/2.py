print('w,x,z,y')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((w or y) and (x <= (not(z))) and (not(w))):
                    print(w,x,y,z,sep='|')