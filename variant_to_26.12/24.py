'''
data = open('24.txt')
listok = data.read()
count = 0
spisokcount = []

for i in range(len(listok)):
    try:
        if listok[i-1] != listok[i] or listok[i] != listok[i+1]:
            count += 1
        else:
            spisokcount.append(count)
            count = 0
    except IndexError:
        pass
print(count)
'''
data = open('24.txt')

spisok = data.read()
spisok = spisok.replace('AAA', '1')
spisok = spisok.replace('BBB', '1')
spisok = spisok.replace('CCC', '1')
spisok = spisok.replace('DDD', '1')
spisok = spisok.replace('EEE', '1')
spisok = spisok.replace('FFF', '1')
spisok = spisok.replace('GGG', '1')
spisok = spisok.replace('HHH', '1')
spisok = spisok.replace('III', '1')
spisok = spisok.replace('JJJ', '1')
spisok = spisok.replace('KKK', '1')
spisok = spisok.replace('LLL', '1')
spisok = spisok.replace('MMM', '1')
spisok = spisok.replace('NNN', '1')
spisok = spisok.replace('OOO', '1')
spisok = spisok.replace('PPP', '1')
spisok = spisok.replace('QQQ', '1')
spisok = spisok.replace('RRR', '1')
spisok = spisok.replace('SSS', '1')
spisok = spisok.replace('TTT', '1')
spisok = spisok.replace('UUU', '1')
spisok = spisok.replace('VVV', '1')
spisok = spisok.replace('WWW', '1')
spisok = spisok.replace('XXX', '1')
spisok = spisok.replace('YYY', '1')
spisok = spisok.replace('ZZZ', '1')
spisok = spisok.replace('000', '1')
spisok = spisok.replace('111', '1')
spisok = spisok.replace('222', '1')
spisok = spisok.replace('333', '1')
spisok = spisok.replace('444', '1')
spisok = spisok.replace('555', '1')
spisok = spisok.replace('666', '1')
spisok = spisok.replace('777', '1')
spisok = spisok.replace('888', '1')
spisok = spisok.replace('999', '1')


count = 0
spisokcount = []
for i in spisok:
    if i != '1':
        count += 1
    else:
        spisokcount.append(count)
        count = 0
print(max(spisokcount))
#doesn't work