sogl = ['С', 'Н', "В", "Д", "Ц"]
count = 0
for i1 in 'ЯСНОВИДЕЦ':
    for i2 in 'ЯСНОВИДЕЦ':
        for i3 in 'ЯСНОВИДЕЦ':
            for i4 in 'ЯСНОВИДЕЦ':
                for i5 in 'ЯСНОВИДЕЦ':
                    s = i1 + i2 + i3 + i4 + i5
                    if s[0] in sogl and s[-1] not in sogl and s.count(s[0]) == 1 and s.count(s[-1]) == 1:
                        count += 1
print(count)