count = 0
for i in 'мечта':
    for i1 in 'мечта':
        for i2 in 'мечта':
            for i3 in 'мечта':
                for i4 in 'мечта':
                    for i5 in 'мечта':
                        s = i + i1 + i2 + i3 + i4 + i5
                        if s.count('а') >= 3:
                            count += 1
print(count)
