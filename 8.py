count = 0 # schet
for x in 'панель':
    for x1 in 'панель':
        for x2 in 'панель':
            for x3 in 'панель':
                for x4 in 'панель':
                    for x5 in 'панель':
                        """ шесть циклов for, поскольку 6 букв """
                        s = x + x1 + x2 + x3 + x4 + x5 # слово, которое получится
                        if 'еап' not in s: # говорим о том, что еап нет в нашем слово
                            if s[0] != 'ь': # первая позиция (буква) не должна быть мягким знаком
                                if s.count('п') == 1 and s.count('а') == 1 and s.count('н') == 1 and s.count('е') == 1 and s.count('л') == 1 and s.count('ь') == 1: # каждая буква должна встретиться ровно 1 раз
                                    count += 1

print(count)