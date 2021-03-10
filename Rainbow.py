import turtle as t
def semi_circle(col,rad,val):
    t.color(col)
    t.circle(rad,-180)
    t.up()
    t.setpos(val,0)
    t.down()
    t.right(180)
window=t.Screen()
col=['violet','indigo','blue','green','yellow','orange','red']
window.bgcolor('black')
t.right(90)
t.width(10)
t.speed(1)
for i in range(7):
    semi_circle(col[i],10*(i+8),-10*(i+1))



