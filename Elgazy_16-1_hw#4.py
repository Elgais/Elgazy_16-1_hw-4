import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.color('red')
p =0 
a= 0
t.penup()
t.goto(0,230)
t.pendown()
t.speed(99999)
while 1:
    t.fd(a)
    t.rt(p)
    a += 4
    p += 1
    if p == 220:
        break
    t.hideturtle()
turtle.done()