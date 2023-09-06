for i in range(0,10**9,999):
    if len(str(i)) == 9:
        s = str(i)
        if s[:2] == '13' and s[-4:-2] == '57' and s[-1] == '9':
            print(i, i // 999)
            