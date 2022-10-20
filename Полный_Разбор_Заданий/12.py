s = '9' * 96 # изначальное число
while '22222' in s or '9999' in s: # условие пока
    if '22222' in s: # если
        s = s.replace('22222', '99', 1) # то
    else:
        s = s.replace('9999','2',1)
print(s)