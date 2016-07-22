from __future__ import division

#Using matrices to transform a wireframe "F"
#8/1/15
#made all the 3x3 vectors into 4x4 to
#allow translation

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

#Vertices of F:
points = np.array([[0, 0, 0,1],
          [ 0, 5, 0,1],
          [ 3,  5, 0,1],
          [3,  4, 0,1],
          [1, 4,  0,1],
          [ 1, 3,  0,1],
          [ 2,  3,  0,1],
          [2,  2,  0,1],
        [1, 2, 0,1],
        [1, 0, 0,1],#9
        [0, 0, 1,1],
          [ 0, 5, 1,1],
          [ 3,  5, 1,1],
          [3,  4, 1,1],
          [1, 4,  1,1],
          [ 1, 3,  1,1],
          [ 2,  3,  1,1],
          [2,  2,  1,1],
        [1, 2, 1,1],
        [1, 0, 1,1]])

f_edges = [[0, 1],[1, 2],[2, 3],[3,4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9],[9, 0],
              [10, 11],[11, 12],[12, 13],[13,14],[14, 15],[15, 16],[16, 17],[17, 18],[18, 19],[19, 10],
              [0,10],[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19]]

#Camera position:
Xc = 0
Yc = 3
Zc = 6

zoom = 10
theta = pi/6
phi = pi/6

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

#Matrix for translation in x, y, and z directions:
t_matrix = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [Tx,  Ty,  Tz,  1]])

forward_matrix = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, -1, 1]])

backward_matrix = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 1]])

right_matrix = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [1, 0, 0, 1]])

left_matrix = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [-1, 0, 0, 1]])

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

def grid(): #draws the x-y grid
    pygame.draw.line(screen,GREEN,[graphx(-8),graphy(0)],[graphx(8),graphy(0)],2)
    pygame.draw.line(screen,GREEN,[graphx(0),graphy(-8)],[graphx(0),graphy(8)],2)
    for i in range(8):#ticks on x-axis
        pygame.draw.line(screen,GREEN,[graphx(8-i),graphy(-0.05)],
                                       [graphx(8-i),graphy(0.05)],2)
    for j in range(8):#ticks on y-axis
        pygame.draw.line(screen,GREEN,[graphx(-0.05),graphy(8-j)],
                                       [graphx(0.05),graphy(8-j)],2)

#without any transformations yet:
newpoints = points

#first rotate the points list across the y-axis:
#newpoints = np.dot(points, r_matrix_Y)

#then rotate the newpoints list across the x-axis:
#newpoints = np.dot(newpoints, r_matrix_X)

#then translate the newpoints list:
#newpoints = np.dot(newpoints, t_matrix)

#Loop until the user clicks the close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#---Main Program Loop ---
#while not done:
tm = time.time()
while not done:
    #---Main event loop
    for event in pygame.event.get():
        mouse_move = pygame.mouse.get_rel()
        theta = mouse_move[1]/10.0
        phi = mouse_move[0]/10.0
        #Matrix for rotation around X-axis
        r_matrix_X = np.array([[1, 0.0,        0.0    ,0],
                             [0.0, cos(theta), sin(theta),0],
                             [0.0, -sin(theta),cos(theta),0],
                               [0.0,     0.0,    0.0,    1]])
        
        newpoints = np.dot(newpoints, r_matrix_X)
        #Matrix for rotation around Y-axis
        r_matrix_Y = np.array([[cos(phi), 0.0,  sin(phi),   0],
                             [0.0,        1,  0.0,       0],
                             [-sin(phi),  0.0,  cos(phi),   0],
                             [0.0,        0.0,  0.0,        1]])
        newpoints = np.dot(newpoints, r_matrix_Y)
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_q:
                done = True
            if event.key == K_w:
                newpoints = np.dot(newpoints, forward_matrix)
            if event.key == K_s:
                newpoints = np.dot(newpoints, backward_matrix)
            if event.key == K_d:
                newpoints = np.dot(newpoints, right_matrix)
            if event.key == K_a:
                newpoints = np.dot(newpoints, left_matrix)

    #First, clear the screen to black.
    screen.fill(BLACK)

    #Draw the x-y grid
    #grid()

    #my idea:
    screen_point = []
    for i in range(len(newpoints)):
        screen_point.append(collapse(newpoints[i]))
        
    #draw the cube by connecting vertices:
    for e in f_edges:
      pygame.draw.line(screen, WHITE, screen_point[e[0]], screen_point[e[1]], 2)

    #Transform the points list again:
    #newpoints = np.dot(newpoints,r_matrix_Y)
    #newpoints = np.dot(newpoints, r_matrix_X)
    #newpoints = np.dot(newpoints, t_matrix)

    #Limit to 60 frames per second
    #clock.tick(30)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
#Close the window and quit
pygame.quit()
