from __future__ import division

'''Using matrices to transform a grid and
3D plot.'''

import pygame
from pygame.locals import *
import time
from math import sin, cos,pi
import numpy as np

#define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
CYAN = (0,255,255)
VIOLET = (148,0,211)

#define function:
points = np.array([[x,4*cos(x),3*sin(x),1] for x in np.arange(-5,5,0.1)])

edges = [[i,i+1] for i in range(len(points)-1)]

#create list of points for drawing the grid
grid_points = [[-6+i,-6,0,1] for i in range(13)]#starting point for vertical lines
end_vert = [[-6+i,6,0,1] for i in range(13)] #ending point for vertical lines
start_horiz = [[-6,-6+j,0,1] for j in range(13)] #starting points for horiz lines
end_horiz = [[6,-6+j,0,1] for j in range(13)] #ending points for horiz lines

#add the points to the list
for point in end_vert:
    grid_points.append(point)

for point in start_horiz:
    grid_points.append(point)

for point in end_horiz:
    grid_points.append(point)
               
grid_edges = [[i, i+13] for i in range(13)]
other_edges = [[j, j+13] for j in range(26,39)]
for edge in other_edges:
    grid_edges.append(edge)

#points for drawing black axes
axes_points = [[-6,0,0,1],[6,0,0,1],[0,-6,0,1],[0,6,0,1]]
axes_edges = [[0,1],[2,3]]

#Camera position:
Xc = 0
Yc = 3
Zc = 10

zoom = 10
theta = 0
phi = 0

#list for 2d version of points:
screen_point = []

#Matrix for rotation around X-axis
r_matrix_X = np.array([[1, 0,        0,     0],
                     [0, cos(theta), sin(theta),0],
                     [0, -sin(theta),cos(theta),0],
                       [0,     0,    0,    1]])

#Matrix for rotation around Y-axis
r_matrix_Y = np.array([[cos(phi), 0,  sin(phi),   0],
                     [0,        1,  0,       0],
                     [-sin(phi),  0,  cos(phi),   0],
                     [0,        0,  0,        1]])

#translation constants
Tx = 0
Ty = 0
Tz = 0

pygame.init()

#set up the display
size = (600,600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Caption")

#Collapses 3D to 2D points
def collapse(point):
    screenx = ((point[0] - Xc) / (point[2] + Zc) * zoom) + Xc
    screeny = ((point[1] - Yc) / (point[2] + Zc) * zoom) + Yc
    return [graphx(screenx),graphy(screeny)]

def graphx(point): #converts coordinate system --> origin in center
    return point*40 + 300

def graphy(point): #converts coordinate system --> origin in center
    return -point*40 + 300 #y-points are reflected over x-axis

def grid(newGridPoints): #draws the x-y grid
    for e in grid_edges:
        pygame.draw.line(screen,GREEN,[graphx(newGridPoints[e[0]][0]),graphy(newGridPoints[e[0]][1])],
                                     [graphx(newGridPoints[e[1]][0]),graphy(newGridPoints[e[1]][1])],2)

def rotate(theta,phi):
    '''Returns matrix for rotation around the x- and y-axes'''
    #Matrix for rotation around X-axis
    r_matrix_X = np.array([[1, 0.0,        0.0    ,0],
                         [0.0, cos(theta), sin(theta),0],
                         [0.0, -sin(theta),cos(theta),0],
                           [0.0,     0.0,    0.0,    1]])
    #Matrix for rotation around Y-axis
    r_matrix_Y = np.array([[cos(phi), 0.0,  sin(phi),   0],
                         [0.0,        1,  0.0,       0],
                         [-sin(phi),  0.0,  cos(phi),   0],
                         [0.0,        0.0,  0.0,        1]])
    return np.dot(r_matrix_X,r_matrix_Y)

def translate(Tx,Ty,Tz):
    '''Returns matrix for translation in the x,y,z directions'''
    #Matrix for translation in x, y, and z directions:
    t_matrix = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [Tx,  Ty,  Tz,  1]])
    return t_matrix

#without any transformations yet:
newpoints = points
newGridPoints = grid_points
newAxesPoints = axes_points

#Loop until the user clicks the close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#---Main Program Loop ---
#while not done:
tm = time.time()
while not done:
    dx = 0
    dy = 0
    dz = 0
    #---Main event loop
    for event in pygame.event.get():
        mouse_move = pygame.mouse.get_rel()
        theta = -mouse_move[1]/100.0
        phi = mouse_move[0]/100.0
        
        #rotate
        newpoints = np.dot(newpoints, rotate(theta,phi))
        newGridPoints = np.dot(newGridPoints, rotate(theta,phi))
        newAxesPoints = np.dot(newAxesPoints, rotate(theta,phi))
     
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_q:
                done = True
            if event.key == K_w:
                dz = 1
            if event.key == K_s:
                dz = -1
            if event.key == K_d:
                dx = 1
            if event.key == K_a:
                dx = -1
            newpoints = np.dot(newpoints, translate(dx,0,dz))
            newGridPoints = np.dot(newGridPoints, translate(dx,0,dz))
            newAxesPoints = np.dot(newAxesPoints, translate(dx,0,dz))

    #First, clear the screen to black.
    screen.fill(WHITE)

    screen_point = []
    screen_grid = []
    screen_axes = []

    #collapse points in function, grid and axes:

    for point in newpoints:
        screen_point.append(collapse(point))
    
    for point in newGridPoints:
        screen_grid.append(collapse(point))

    for point in newAxesPoints:
        screen_axes.append(collapse(point))

    #Draw the x-y grid
    #grid(newGridPoints)
    for e in grid_edges:
        pygame.draw.line(screen,CYAN,[screen_grid[e[0]][0],screen_grid[e[0]][1]],
                                     [screen_grid[e[1]][0],screen_grid[e[1]][1]],2)

    #draw the axes
    pygame.draw.line(screen, BLACK, screen_axes[0],screen_axes[1],3)
    pygame.draw.line(screen, BLACK, screen_axes[2],screen_axes[3],3)

    #draw the function by connecting vertices:
    for e in edges:
        pygame.draw.line(screen, VIOLET, screen_point[e[0]], screen_point[e[1]], 3)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
#Close the window and quit
pygame.quit()
