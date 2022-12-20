a = 'аимнр'
count = 0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a:
                    s = i1 + i2 + i3 + i4 + i5
                    count +=1
                    if s == 'наири':
                        print(count)