data = open('24.txt')
spisok = data.read()
letter = {

}
s = ''
maxim = 0
word = ''
for i in range(len(spisok)-2):
    if spisok[i] == 'X' and spisok[i+2] == 'Z':
        if spisok[i+1] in letter:
            letter[spisok[i+1]].append(1)
        else:
            letter[spisok[i+1]] = [1]

for i in letter:
    if len(letter[i]) > maxim:
        maxim = len(letter[i])
        word = i
print(maxim, word)
