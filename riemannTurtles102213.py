from turtle import *

def f(x):
	return -0.2*x**5 + 1.4*x**4+x**3-5*x**2-1.5*x + 5 #constant was 1.4

def tick():
	lt(90)
	fd(.1)
	bk(.2)
	fd(.1)
	rt(90)

def setup(startingx, endingx):
	speed(10)
	setworldcoordinates(-5,-5,5,5)
	setpos(0,0)
	color("black")
	pd()
	for i in range(4):
		for j in range(5):
			fd(1)
			tick()
		bk(5)
		rt(90)


def posxy(startingx):
	speed(1000000)
	pu()
	setpos(startingx,f(startingx))
	pd()
	dx = 0.01
	setheading(0)
	while xcor()<7:
		goto(xcor()+0.05,f(xcor()+0.05))
	pu()   

def rectangle(startingx,width):
	pu()
	setpos(startingx,0)
	setheading(90)
	color("black","red")
	pd()
	begin_fill()
	height = f(xcor())
	fd(height)
	rt(90)
	fd(width)
	rt(90)
	fd(height)
	setheading(0)
	end_fill()

def riemann(startingx,endingx,numberofRectangles):
	area = 0
	absarea = 0
	width = (float(endingx) - float(startingx))/ numberofRectangles
	for i in range(numberofRectangles):
		area1 = f(startingx+i*width)*width
		area += area1
		absarea += abs(area1)
	print(area, absarea)

def lefthand(startingx, endingx,numberofRectangles):
	setworldcoordinates(-5,-5,5,5)
	setup(startingx,endingx)
	posxy(startingx - 3)
	width = (float(endingx) - float(startingx))/ numberofRectangles
	setpos(startingx,0)
	area = 0
	absarea = 0 #absolute value of the area
	for i in range(numberofRectangles):
		rectangle(xcor(),width)
		area1 = f(xcor())*width
		area += area1
		absarea += abs(area1)
	print(area, absarea)

lefthand(-1,2,25)
exitonclick()
