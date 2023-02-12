a = 3
p = ''
while a:
    p += str(a % 5)
    a//=5
print('-'+ p[::-1])