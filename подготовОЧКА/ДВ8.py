a = 'иклнор'
count = 0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                count += 1
                s = i1 + i2 + i3 + i4
                if s == 'кино':
                    print(count)