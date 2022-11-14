for i1 in range(10):
    for i2 in range(10):
        s = int(f'12345{i1}6{i2}8')
        if s % 17 == 0:
            print(s, s / 17)
