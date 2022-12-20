from turtle import *
color('black', 'red')
m = 100
begin_fill()
left(90)
right(45)
for i in range(4):
    forward(55*m)
    right(90)
end_fill()
canvas = getcanvas()
count = 0
for y in range(-100*m,100*m,m):
    for x in range(-100*m,100*m,m):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
done()
exit()