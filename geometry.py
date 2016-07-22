from turtle import *
from math import sqrt,pi
from arithmetic import average
from algebra import setup,graph,equation, quad

def draw_circle(center,radius):
    '''draws a circle with given center and radius'''
    speed(0)
    pu()
    goto(center)    #First go to the center
    shape('circle') #set turtle to circle shape 
    clone()         #Leave a point at the center  
    fd(radius)      #move to the circumference
    lt(90)          #turn to move along the edge
    arc_length = 2*pi*radius/360 #length of segment on arc
    pd()            #put pen down to draw
    for i in range(360): #"do this 360 times"
        fd(arc_length)  #draw the segment
        lt(1)           #turn a little
    ht()            #hide turtle

def line2points(point1,point2):
    '''Returns the slope and y-intercept of
    the line between two points'''
    slope = (point2[1] - point1[1])/(point2[0] - point1[0])
    y_int = point1[1] - slope*point1[0]
    return slope, y_int

#Graphs two points and the line between them
def line2points2(point1,point2):
    speed(0)
    line = line2points(point1, point2)
    slope = line[0]
    yintercept = line[1]
    setup()
    pu()
    goto(point1)
    shape("circle")
    clone()
    goto(point2)
    clone()
    def f(x):
        return slope*x + yintercept
    graph(f)
    print("y =",slope, "x +",yintercept)

def midpt(point1,point2):
    '''Returns the midpoint of two points'''
    return average(point1[0],point2[0]),average(point1[1],point2[1])

def intersection(a,b,c,d):
    '''Returns the intersection of two lines y = ax + b
    and y = cx + d'''
    x = equation(a,b,c,d) #solve for x
    y = a*x + b  #plug x in to find y
    return (x,y)

def graphIntersection(slope1, yintercept1,slope2,yintercept2):
    '''Graphs 2 lines and their intersection'''
    speed(0)
    intpoint = intersection(slope1, yintercept1,slope2,yintercept2)
    print (intpoint)
    setup()
    pu()
    goto(intpoint)
    shape("circle")
    clone()
    def f(x):
        return slope1*x + yintercept1
    graph(f)
    def g(x):
        return slope2*x + yintercept2
    graph(g)

def distance(point1,point2):
    '''Returns the distance between two points'''
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - \
                point2[1])**2)

def heron(side1,side2,side3):
    '''Returns the area of a triangle given 3 side lengths'''
    semi = (side1 + side2 + side3)/2
    return sqrt(semi*(semi - side1)*(semi - side2)*(semi - side3))

def heronPoints(point1,point2,point3):
    '''Returns the area of a triangle given 3 side lengths'''
    side1 = distance(point1,point2)
    side2 = distance(point2,point3)
    side3 = distance(point1,point3)
    return heron(side1,side2,side3)

def line(slope,point):
    '''Returns the slope and y-intercept of a line
    with the given slope through the given point'''
    return slope, point[1]-slope*point[0]

def negative_recip(number):
    '''Returns the negative reciprocal of a number'''
    return -1/number

def perpend_line(slope,point):
    '''Returns the slope and y-intercept of a line
    perpendicular to a line with given slope
    through given point'''
    return line(negative_recip(slope),point)

def perp_bisect(point1, point2):
    '''Returns the slope and y-intercept of the
    Perpendicular Bisector of 2 points'''
    line = line2points(point1,point2)
    midpoint = midpt(point1,point2)
    return perpend_line(line[0],midpoint)

def graphPerpBisect(point1,point2):
    '''graphs two points and the perpendicular bisector
    of the segment between them'''
    setup()
    speed(0)
    pu()
    goto(point1)
    shape("circle")
    clone()
    pd()
    goto(point2)
    clone()
    pu()
    line = perp_bisect(point1,point2)
    def f(x):
        return line[0]*x + line[1]
    graph(f)

def dist_point_line(point, slope, y_intercept):
    '''Returns the distance from a point to a line
    Line should be entered as slope, y-intercept'''
    perp_line = perpend_line(slope,point)
    #from the intersection function:
    intersect = intersection(slope, y_intercept, perp_line[0], perp_line[1])
    dist = distance(intersect,(point))
    return dist


def equid_pt(point1,point2,point3):
    '''Returns the coordinates of the point
    equidistant to three points'''
    line1 = perp_bisect(point1,point2)
    line2 = perp_bisect(point2,point3)
    return intersection(line1[0],line1[1],line2[0],line2[1])


def circumcircle(point1,point2,point3):
    '''Returns the center and radius of the circumcircle
    of a triangle given 3 points'''
    center = equid_pt(point1,point2,point3)
    radius = distance(center,point1)
    print("center: ",center)
    print("radius: ",radius)
    shape("circle")
    pu()
    goto(point1)
    st()
    clone()
    goto(point2)
    #st()
    clone()
    goto(point3)
    #st()
    clone()
    draw_circle(center,radius)

#Returns the centroid of a triangle given 3 points
def centroid(point1,point2,point3):
    median1 = line2points(midpt(point1,point2),point3)
    median2 = line2points(midpt(point3,point2),point1)
    return intersection(median1[0],median1[1],median2[0],median2[1])

#Returns the vertex of y = a*x**2 + b*x + c
def vertex(a,b,c):
    #This finds the axis of symmetry
    h = b/(2.*a) 
    # plug in to find y-value of vertex
    k = a*h**2 - b*h + c
    print("The vertex is (",h, ",",k, ")")
