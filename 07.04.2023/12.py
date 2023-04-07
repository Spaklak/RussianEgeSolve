for i in range(50):
    for x in range(50):
        for z in range(50):
            s = '0' + '1' * i + '2' * x + '3' * z + '0'
            k = s
            while '00' not in s:
                s = s.replace('01', '21022', 1)
                s=s.replace('02', '310', 1)
                s = s.replace('03', '230112')
            if s.count('1') == 96 and s.count('2') == 36 and s.count('3') == 80:
                print(len(k))