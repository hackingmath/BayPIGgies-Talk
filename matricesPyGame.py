#Grapher with tick marks at whole numbers
import pygame
from pygame.locals import *
from math import pi, acos, cos, sin

#Converts degrees to radians:
def convToRads(degrees):
    return degrees*pi/180

#Converts radians to degrees:
def convToDegs(radians):
    return radians*180/pi

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
VIOLET = (148,0,211)

XMIN = -8
XMAX = 8
YMIN = -8
YMAX = 8

WIDTH = 600
HEIGHT = 600
size = (HEIGHT,WIDTH)

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

edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,0]]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Transforming with Matrices')

def graphXY(point):
    '''converts xy coords to pygame coords'''
    return [point[0]*WIDTH/(XMAX-XMIN)+WIDTH/2,
            -point[1]*HEIGHT/(YMAX-YMIN)+HEIGHT/2]

def drawf(m,color):
    '''draws lines between the points in matrix m'''
    for e in edges:
        pygame.draw.line(screen,color,graphXY(m[e[0]]),
                                     graphXY(m[e[1]]),2)
    
def grid():
    #cyan lines. Horizontal
    for i in range(XMAX-XMIN+1):
        pygame.draw.line(screen,CYAN,graphXY([XMIN,YMIN+i]),
                                    graphXY([XMAX,YMIN+i]),2)
        #Vertical:
        pygame.draw.line(screen,CYAN,graphXY([XMIN+i,YMIN]),
                                    graphXY([XMIN+i,YMAX]),2)

    pygame.draw.line(screen,BLACK,graphXY([XMIN,0]),
                                graphXY([XMAX,0]),2)
    pygame.draw.line(screen,BLACK,graphXY([0,YMIN]),
                                graphXY([0,YMAX]),2)
    
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
    rotmatrix = [[cos(rads),sin(rads)],
                    [-sin(rads),cos(rads)]]
    return rotmatrix

rotmat = multMatrix(fmatrix,rotate(5))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    mouse_move = pygame.mouse.get_rel()
    rot = mouse_move[0]
    
    screen.fill(WHITE)

    grid()
    drawf(fmatrix,VIOLET)

    #Define Transformation matrix:
    transmatrix = [[0,-1],
                    [1,1]]

    #Multiply F-matrix by transformation matrix
    newmat = multMatrix(fmatrix,transmatrix)

    #Multiply F-matrix by rotation matrix
    rotmat = multMatrix(rotmat,rotate(rot))

    drawf(rotmat,RED)

    pygame.display.update()

pygame.quit()
