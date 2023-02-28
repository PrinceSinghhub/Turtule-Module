import turtle
t=turtle.Turtle()
m=1
for i in range(360):
    t.speed(0)
    t.pendown()
    t.right(m)
    t.forward(100)
    t.right(30)
    t.forward(60)
    t.left(30)
    t.forward(30)
    t.penup()
    t.home()
    m+=1
