from turtle import *
from time import sleep
screen=Screen()
speed(0)
screen.bgcolor('black')
colormode(255)
red=(223,35,35);green=(75,183,75);yellow=(252,210,9);blue=(86,146,195)
r=120
speed(0)
seth(-150)
up()

#--------------red petal=======
color(red)
begin_fill()
fd(r)
down()
right(90)
circle(-r,120)
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
end_fill()

#============green petal----

left(180)
color(green)
begin_fill()
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
left(180)
circle(-r,120)
end_fill()

#---------------yellow petal-------

left(180)
circle(r,120)
color(yellow)
begin_fill()
circle(r,120)
right(180)
fd(r*3**.5)
right(60)
circle(-2*r,120)
right(120)
fd(r*3**.5)
end_fill()

#---------------last patel --------------

screen=getscreen()
clear()
ht()
up()
goto(-300,0)
color("Yellow")
write("CODEX CODER", font=("Arial",30,"bold"))
goto(160,0)
