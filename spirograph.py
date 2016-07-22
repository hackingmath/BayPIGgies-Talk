#Spirograph via Trigonometric Delights

from turtle import *
from math import sin, cos

clear()
pu()
theta = 0
R = 200.0 #inner radius of big ring
r = 50.0 #radius of small disk. Change this one
p = 0.75 #How close the "hole" is to the center
color("red")
pensize(2)
for i in range(5000):
    speed(0)
    #Here are the position formulas for the "pen" point:
    x = (R -r)*cos(theta)+p*r*cos(((R-r)/r)*theta)
    y = (R -r)*sin(theta)-p*r*sin(((R-r)/r)*theta)
    goto(x,y)#send the turtle to that position
    pd()
    theta += 0.1 #increase theta by a bit

exitonclick()
