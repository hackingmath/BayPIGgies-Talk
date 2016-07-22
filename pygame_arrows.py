from __future__ import division

#The Arrow Field in Pygame
#matrix.py is my file


import pygame
from pygame.locals import *
import time
from math import pi
import numpy as np
import matrix

#define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

a_edges = [[0, 1],[1, 2],[2, 3],[3,4],[4, 5],[5, 6],[6, 0]]

arrows = []

class Arrow:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

        #Vertices of arrow:
        self.points = np.array([[self.x, self.y,1],
                          [ self.x, self.y + self.length/3.5,1],
                          [ self.x + 2*self.length/3.5, self.y + self.length/3.5,1],
                          [ self.x + 2*self.length/3.5, self.y + 1.75*self.length/3.5,1],
                          [ self.x + self.length, self.y + 0.5*self.length/3.5,1],
                          [ self.x + 2*self.length/3.5, self.y - 0.75*self.length/3.5,1],
                          [ self.x + 2*self.length/3.5, self.y,1]])

    def draw(self):
        target_point = pygame.mouse.get_pos()
        rotatedMatrix = matrix.matrixRotate(self.points,target_point)
        graphPoints = []
        for row in rotatedMatrix:
            graphPoints.append([row[0],row[1]])

        for e in a_edges:
            pygame.draw.line(screen, WHITE, graphPoints[e[0]], graphPoints[e[1]], 2)


pygame.init()

#set up the display
size = (600,600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Arrow Field")

for i in range(20):
    for j in range(20):
        arrows.append(Arrow(30*i+10, 30*j+10, 20))

#Loop until the user clicks the close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#---Main Program Loop ---
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #---Main event loop

    #First, clear the screen to black.
    screen.fill(BLACK)

    #draw the arrows
    for arrow in arrows:
        arrow.draw()

    #Limit to 60 frames per second
    #clock.tick(30)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

#Close the window and quit
pygame.quit()
