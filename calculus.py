'''Calculus Chapter of Hacking Math Class'''

from turtle import *
from algebra import setup, graph
from geometry2 import line,perpendicularLine, intersection

speed(0)

def f(x):
    return -0.2*x**5 + 1.4*x**4+x**3-5*x**2-1.5*x + 3

def derivative(a):
    '''Returns the derivative of a function at point x = a'''
    dx = 0.00001 #the tiny "run"
    dy = f(a + dx) - f(a)
    return dy/dx
    
#print("Derivative of f(x) at 3 is ",derivative(3))

def newton(guess):
	'''Approximates the roots of a 
	function using the derivative'''
	for i in range(20):
		new_guess = guess - f(guess)/derivative(guess)
		guess = new_guess
		print(new_guess)
	
#newton(1.5)

def newtonTurtle(guess):
	setup()
	graph(f)
	pu()
	goto(guess,0)
	pd()
	for i in range(5):
		goto(guess,f(guess))
		d=derivative(guess)
		line2 = line(d,(guess,f(guess)))
		goto(intersection(line2[0],line2[1],0,0))
		new_guess = guess - f(guess)/derivative(guess)
		guess = new_guess
	
#newtonTurtle(1.5)
	
def nint(f,startingx, endingx, number_of_rectangles):
    '''returns the area under a function'''
    sum_of_areas = 0 #running sum of the areas
    #width of every rectangle:
    width = (endingx - startingx) / number_of_rectangles
    for i in range(number_of_rectangles):
        height = f(startingx + i*width)
        area_rect = width * height
        sum_of_areas += area_rect
    return sum_of_areas


def trapezoid(startingx, endingx,numberofTrapezoids):
    '''Returns the area under a function
    using Trapezoidal Method'''
    width = (float(endingx) - float(startingx))/ numberofTrapezoids
    area = 0
    for i in range(numberofTrapezoids):
    #backslash simply continues the code on the next line:
        area1 = 0.5*width*(f(startingx + i*width)+\
                          f((startingx + i*width)+width))
        area += area1
    print(area)

def trap(f,startingx,width):
    '''draws one trapezoid'''
    pu()        #pen up
    speed(0)    		#fastest speed
    setpos(startingx,0) #go to the starting x-coordinate
    setheading(90)  #face straight up
    color("black","red")    
    pd()        		#put your pen down
    begin_fill()    	#start filling in the trapezoid
    height = f(xcor()) #height of the trapezoid
    fd(height)  		#go to the top of the trapezoid
    setpos(xcor()+width,f(xcor()+width)) # down the "slant"
    sety(0) 		#straight down to the x-axis
    setheading(0) 	#face right
    end_fill()    	#stop filling the trapezoid

def trapezoid2(f,startingx, endingx,numberofTrapezoids):
    '''Calculates area under function f between
    startingx and endingx using trapezoids and graphs it'''
    speed(0)
    setup()
    graph(f)
    pu()
    width = (float(endingx) - float(startingx))/ numberofTrapezoids
    setpos(startingx,0)
    pd()
    area = 0
    for i in range(numberofTrapezoids):
        trap(f,xcor(),width) #draw a trapezoid
        area1 = 0.5*width*(f(startingx + i*width)+f((startingx + \
                               i*width)+width))
        area += area1 #update the running sum of the area
    print(area)

trapezoid2(f,-1,2,10)
#Runge-Kutta Method for solving DEs

def deriv(x,y):
    return x**2 + y**2

def rk4(x0,y0,h): #order 4
    while x0 <= 1.0:
        print(x0,y0)
	  # I changed the l's to m's
        m1 = h*deriv(x0,y0)
        m2 = h*deriv(x0 + h/2, y0 + m1/2)
        m3 = h*deriv(x0 + h/2, y0 + m2/2)
        m4 = h*deriv(x0 + h, y0 + m3)
	   #These are the values that are fed back into the function:
        y0 = y0 + (1/6)*(m1 + 2*m2 + 2*m3 + m4)
        x0 = x0 + h

exitonclick()
