from turtle import *
from algebra import setup,graph

def f(x):
    return 4 - x**2#(1+x**2)**(0.25)

def trap(startingx, width):
    pu()
    speed(0)
    setpos(startingx,0)
    seth(90)
    color("black","red")
    pd()
    begin_fill()
    height = f(xcor())
    fd(height)
    setpos(xcor()+width, f(xcor()+width))
    sety(0)
    setheading(0)
    end_fill()

def trapezoid(startingx,endingx,numberofTrapezoids):
    speed(0)
    setup()
    graph(f)
    pu()
    setpos(startingx,0)
    pd()
    width = (float(endingx) - float(startingx))/numberofTrapezoids
    setpos(startingx,0)
    color("green")
    area = 0
    for i in range(numberofTrapezoids):
        trap(xcor(), width)
        area1 = 0.5*width*(f(startingx+i*width)+f((startingx+i*width)+width))
        area += area1
    print area
