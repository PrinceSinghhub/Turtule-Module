import turtle as t
import random
t.colormode(255)
t.speed(10)
t.pensize(1)
for i in range(5):
    # r=random.randint(0,255)
    # g = random.randint(0,255)
    # b = random.randint(0,255)
    t.fillcolor("red")
    # t.color(r,g,b)
    t.begin_fill()
    t.circle(30*i)
    t.penup()
    t.goto(0,-30*i)
    t.pendown()
    t.end_fill()

