# согл: с н в д ц
# глас: я о и е
count = 0
for i1 in 'ясновидец':
    for i2 in 'ясновидец':
        for i3 in 'ясновидец':
            for i4 in 'ясновидец':
                for i5 in 'ясновидец':
                    s = i1 + i2 + i3 + i4 + i5
                    if ((s[0] == 'с' and s.count('с') == 1) or (s[0] == 'н' and s.count('н') == 1) or (s[0] == 'в' and s.count('в') == 1) or (s[0] == 'д' and s.count('д') == 1) or (s[0] == 'ц' and s.count('ц') == 1)) and\
                    ((s[4] == 'я' and s.count('я') == 1) or (s[4] == 'о' and s.count('о') == 1) or (s[4] == 'и' and s.count('и') == 1) or (s[4] == 'е' and s.count('е') == 1)):
                        count += 1
print(count)