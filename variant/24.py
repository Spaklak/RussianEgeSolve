from numpy import number


data = open('24.txt')
spisok = [x for x in data.read()]
numbers = ['0','1','2','3','4','5','6','7','8','9']
count = 0
s = ''
for i in spisok:
    s = s + i
    if i in numbers:
        if len(s) == 6 and s[0] in numbers:
            count += 1 
            s = i
        else:
            s = i
print(count)