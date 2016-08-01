#Grapher with tick marks at whole numbers
from turtle import *
from math import pi, acos, cos, sin
speed(0)

#Converts degrees to radians:
def convToRads(degrees):
    return degrees*pi/180

#Converts radians to degrees:
def convToDegs(radians):
    return radians*180/pi

def mark():
    rt(90)
    fd(0.1)
    bk(0.2)
    fd(0.1)
    lt(90)
    
def setup():
    speed(0) #Sets turtle speed to fastest
    setworldcoordinates(-5,-5,7,7) #lower left and upper right corners
    setpos(0,0)     #sets turtle’s position to (0,0)
    clear()         #Clears its trails
    setheading(0)   #Faces the right of the screen
    pd()            #Puts its pen down to draw
    color("black")  #Sets its color to black    
    for i in range(4):  #”Do this four times”
        setpos(0,0)     #Centers itself again
        for j in range(7): #Make 7 tick marks
            fd(1)       
            mark()      
        rt(90)          
    pu()            #Sets its pen in up position

#This draws the F
fmatrix = [[0,0],
            [1,0],
            [1,2],
            [2,2],
            [2,3],
            [1,3],
            [1,4],
            [3,4],
            [3,5],
            [0,5],
           [0,0]]

def drawf(matA):
    pu()
    goto(0,0)
    pd()
    for point in matA: #the turtle goes to all the points in the list
        goto(point[0],point[1])

def multMatrix(a,b):
    '''Multiplies two matrices.
    b is a 2x2 matrix'''
    newmatrix = []
    for i in range(len(a)): #because our f-matrix has 11 rows
        newmatrix.append([])
        for j in range(2):
            newmatrix[i].append(a[i][0]*b[0][j]+a[i][1]*b[1][j])
    return newmatrix

#Returns the matrix for rotating "degrees" degrees
def rotate(degrees):
    rads = convToRads(degrees)
    #Define Rotation matrix:
    rotmatrix = [[cos(rads),-sin(rads)],
                    [sin(rads),cos(rads)]]
    return rotmatrix

#Define Transformation matrix:
transmatrix = [[0,-1],
                [1,1]]

#Multiply F-matrix by transformation matrix
newmat = multMatrix(fmatrix,transmatrix)

#Multiply F-matrix by rotation matrix
#We’ll start off testing a 45 degree rotation
rotmat = multMatrix(fmatrix,rotate(120))

pensize(1)
setup()
color('blue')
drawf(fmatrix)
pensize(2) #makes transformed F thicker
color('red')
drawf(rotmat)
