'''Geometry Functions'''

from turtle import *
from math import pi,sqrt

#from algebra import setup,graph,equation

def equation(a,b,c,d):
    '''Returns the solution of an equation
    of the form ax + b = cx + d'''
    return (d - b)/(a - c)
    
    
def mark():
    rt(90)
    fd(0.1)
    bk(0.2)
    fd(0.1)
    lt(90)
    
def setup():
    speed(0) #Sets turtle speed to fastest
    setworldcoordinates(-6,-5,6,5) #lower left and upper right corners
    setpos(0,0)     #sets turtle's position to (0,0)
    clear()         #Clears its trails
    setheading(0)   #Faces the right of the screen
    pd()            #Puts its pen down to draw
    color("black")  #Sets its color to black    
    for i in range(4):  #"Do this four times"
        setpos(0,0)     #Centers itself again
        for i in range(6): #Make 5 tick marks
            fd(1)       
            mark()      
        rt(90)          
    pu()            #Sets its pen in up position

def f(x):           #This defines the function f(x)
    #return 2*x + 3  #The line y = 2x + 3
    return 2*x**2+7*x-11#6*x**3 + 31*x**2+3*x-10

def graph(f):    #The function f(x) has to be defined
    speed(0)    #Sets speed to the fastest
    color("black")  #Sets its color
    setpos(-6,f(-6))    #Sets its position to the left edge
    pd()                #pen down
    setheading(0)       #Face right
    x = xcor()	#set a variable, x, to the x-coordinate of the turtle
    while xcor() <= 6:  #Do this until the x-coordinate is more than 6
        x += 0.01       #make x go up a tiny bit
        goto(x,f(x))    #Go to the next point on the graph

def drawCircle(center,radius):
    '''draws a circle with a given
    center and radius'''
    speed(0)
    pu()
    goto(center)
    shape('circle')
    clone()
    fd(radius)
    lt(90)
    arc_length = 2*pi*radius/360
    pd()
    for i in range(360):
        fd(arc_length)
        lt(1)
    ht()
    
def line2points(point1,point2):
    '''Returns the slope and y-intercept of
    the line between two points'''
    slope = (point2[1]-point1[1])/(point2[0]-point1[0])
    y_int = point1[1] - slope*point1[0]
    return slope, y_int

def line2points2(point1,point2):
    '''Graphs 2 points and the line
    between them.'''
    slope, y_int = line2points(point1,point2)
    setup()
    pu()
    goto(point1)
    shape('circle')
    clone()
    goto(point2)
    clone()
    def f(x):
        return slope*x + y_int
    graph(f)
    print("y=",slope,"x + ",y_int)
    
def average(a,b):
	'''returns the average of a and b'''
	return (a + b)/ 2

def midpoint(point1,point2):
    '''returns the midpoint of two points'''
    return average(point1[0],point2[0]),average(point1[1],point2[1])


def intersection(a,b,c,d):
    '''returns the intersection of the two lines y = ax + b
    and y = cx + d'''
    x = equation(a,b,c,d) #solve for x
    y = a*x + b #plug in x to find y
    return (x,y)

def graphIntersection(slope1,y_int1,slope2,y_int2):
    '''Graphs two lines and their intersection'''
    intpoint = intersection(slope1,y_int1,slope2,y_int2)
    print(intpoint)
    setup()
    pu()
    goto(intpoint)
    shape('circle')
    clone()
    def f(x):
        return slope1*x + y_int1
    graph(f)
    pu()
    def g(x):
        return slope2*x + y_int2
    graph(g)
    
def line(slope,point):
    '''Returns the slope and y-intercept of the line
    with the given slope through the given point'''
    return slope, point[1]-slope*point[0]

def negativeRecip(number):
    return -1/number

def perpendicularLine(slope,point):
    '''Returns the slope and y-intercept of a line
    perpendicular to a line with the given slope
    through the given point'''
    return line(negativeRecip(slope),point)

def perpBisect(point1,point2):
    '''Returns the slope and y-intercept of the
    Perpendicular Bisector of 2 points'''
    line = line2points(point1,point2)
    midpt = midpoint(point1,point2)
    return perpendicularLine(line[0],midpt)

def graphPerpBisect(point1,point2):
    setup()
    pu()
    goto(point1)
    shape('circle')
    clone()
    pd()
    goto(point2)
    clone()
    pu()
    line = perpBisect(point1,point2)
    def f(x):
        return line[0]*x + line[1]
    graph(f)

def equidPt(point1,point2,point3):
    '''Returns the coordinates of the point
    equidistant to three points'''
    line1 = perpBisect(point1,point2)
    line2 = perpBisect(point2,point3)
    return intersection(line1[0],line1[1],line2[0],line2[1])

def distance2pts(point1,point2):
    '''returns the distance between two points'''
    return sqrt((point1[0]-point2[0])**2 + (point1[1]- \
                point2[1])**2)

def circumcircle(point1,point2,point3):
    '''Returns the center and radius of the circumcircle
    of a triangle given 3 points.'''
    center = equidPt(point1,point2,point3)
    radius = distance2pts(center,point1)
    setup()
    shape('circle')
    pu()
    goto(point1)
    st()
    clone()
    goto(point2)
    clone()
    goto(point3)
    clone()
    drawCircle(center,radius)
    return center, radius
    
circumcircle((-1,2),(2,3),(1,-4.5))

exitonclick()
