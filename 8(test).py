from itertools import count


a = 'крыша'
count = 0
for i1 in 'крыша':
    for i2 in 'крыша':
        for i3 in 'крыша':
            for i4 in 'крыша':
                for i5 in 'крыша':
                    for i6 in 'крыша':
                        s = i1 + i2 + i3 + i4 + i5 + i6
                        if s.count('ы') <= 2 and s.count('а') <= 2:
                            if not 'р' in s and not 'ш' in s and s.count('к') <= 1 and s[0] == 'к':
                                count += 1
                            elif not 'к' in s and not 'ш' in s and s.count('р') <= 1 and s[0] == 'р':
                                count += 1
                            elif not 'р' in s and not 'к' in s and s.count('ш') <= 1 and s[0] == 'ш':
                                count += 1
                            elif not 'к' in s and not 'р' in s and not 'ш' in s:
                                count += 1

print(count)