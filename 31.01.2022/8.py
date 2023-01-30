count = 0
for i1 in range(1,16, 2):
    for i2 in range(0,16,2):
        for i3 in range(1,16, 2):
            for i4 in range(0,16,2):
                for i5 in range(1,16, 2):
                    for i6 in range(0,16,2):
                        for i7 in range(1,16, 2):
                            for i8 in range(0,16,2):
                                for i9 in range(1,16, 2):
                                    for i10 in range(0,16,2):
                                        for i11 in range(1,16, 2):
                                            for i12 in range(0,16,2):
                                                if i1 >= i2 and i2 >= i3 and i3 >= i4 and i4 >= i5 and i5 >= i6 and i6 >= i7 and i7 >= i8 and i9 >= i10 and i11 >= i12:
                                                    count += 1
                                                    
print(count)