a = 'авелрфь'
count = 0
b = []
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a:
                    for i6 in a:
                        count += 1
                        s = i1 + i2 + i3 + i4 + i5 + i6
                        if 'а' not in s and 'е' not in s:
                            b.append(count)

print(min(b))