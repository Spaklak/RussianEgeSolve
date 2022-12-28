for i in range(1,1000):
    forseven = i
    forsix = i
    for13 = i
    forsevenspis = ''
    sorsixspis = ''
    for13spis = ''
    while forseven:
        forsevenspis += str(forseven % 7)
        forseven //= 7
    while forsix:
        sorsixspis += str(forsix % 6)
        forsix //= 6
    while for13:
        for13spis += str(for13 % 13)
        for13 //= 13
    if len(forsevenspis) == 2 and len(sorsixspis) == 3 and for13spis[0] == '3':
        print(i)