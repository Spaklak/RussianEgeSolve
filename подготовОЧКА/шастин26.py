# 5000 - N (кол-во привезенной продукции)
# 500 - K (кол-во холодосов)
# 6000 - M (вместительность холодосов)
'''
поставить - и вычесть единицу
'''
data = open('26.txt')
data = [int(x) for x in data.read().split()]
data.sort()
was = 0
k = 1
data = data[::-1] # от большего к меньшему
for i in range(len(data)):
    if was + data[i] < 6000:
        was += data[i]
        data[i] = 0
    elif was + data[i] > 6000:
        for x in range(len(data)):
            if was + data[-x-1] < 6000:
                was += data[-x-1]
                data[-x-1] = 0
            elif was + data[-x-1] == 6000:
                k += 1
                data[-x-1] = 0
                was = data[i]
                data[i] = 0
                break
            elif was + data[-x-1] > 6000:
                was = data[i]
                k += 1
                data[i] = 0
                break
    else:
        was = 0
        k += 1
        data[i] = 0

print(k)
print(6000-was)