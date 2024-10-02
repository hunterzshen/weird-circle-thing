from random import *
from turtle import *

def chase():
    for i in range(1,150):
        angle = chasers[i].towards(chasers[i-1])
        chasers[i].seth(angle)
    for i in range(1,150):
        chasers[i].fd(10)
    s.update()
    chasers[0].left(5)
    chasers[0].fd(10)

    for i in range(151,n):
        angle = chasers[i].towards(chasers[i-1])
        chasers[i].seth(angle)
    for i in range(151,n):
        chasers[i].fd(10)
    s.update()
    chasers[150].right(5)
    chasers[150].fd(10)

    s.ontimer(chase,10)

s=Screen()
s.tracer(0)
n=300
chasers = []
for i in range(n):
    chasers.append(Turtle())
    colormode(255)
    chasers[i].color( randint(0,255), randint(0,255), randint(0,255))
    chasers[i].penup()
    chasers[i].goto(randint(-300,300), randint(-300,300))
chasers[0].goto(0,0)
chasers[0].color('red')
chasers[0].shape('circle')
chasers[150].goto(0,0)
chasers[150].color('blue')
chasers[150].shape('circle')
s.update()



chase()
update()
