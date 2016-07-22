from turtle import *
speed(0)

def square(length):
	for i in range(4):
		fd(length)
		rt(90)
		
def spiral():
	length = 5
	for i in range(70):
		square(length)
		rt(5)
		length += 5
		

def astroid():
	color('violet')
	pu()
	goto(-300,0)
	pd()
	for j in range(0,300,10):
		goto(0,j)
		goto(-300+j,0)
		goto(0,-j)
	for j in range(0,300,10):
		goto(0,j)
		goto(300-j,0)
		goto(0,-j)

spiral()	
#astroid()

exitonclick()
