from __future__ import division

import pygame
from pygame.locals import *
import time
from math import pi
import numpy as np


#define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

a_edges = [[0, 1],[1, 2],[2, 3],[3,4],[4, 5],[5, 6],[6, 0]]

arrows = []

def add_arrow(x, y, length):
  global arrows
  #Vertices of arrow:
  arrows.extend([[x, y, x, y],
           [x, y, x, y + length/3.5],
           [x, y, x + 2*length/3.5, y + length/3.5],
           [x, y, x + 2*length/3.5, y + 1.75*length/3.5],
           [x, y, x + length, y + 0.5*length/3.5],
           [x, y, x + 2*length/3.5, y - 0.75*length/3.5],
           [x, y, x + 2*length/3.5, y]])

def draw_arrows():
  global np_arrows
  target_point = pygame.mouse.get_pos()
  rotatedMatrix = matrixRotate(np_arrows, target_point)
  for i in range(0, len(rotatedMatrix), 7):
    for e in a_edges:
      pygame.draw.line(screen, WHITE, rotatedMatrix[i + e[0]], rotatedMatrix[i + e[1]], 2)

def matrixRotate(matA, point):
    rot_angle = np.arctan2(point[1] - matA[:,1], point[0] - matA[:,0])
    ca = np.cos(rot_angle) # save typing and halve trig calls
    sa = np.sin(rot_angle)
    matB = np.copy(matA[:,2:]) - matA[:,0:2] # translate to origin
    tmp = matB[:,0] * ca - matB[:,1] * sa # save overwriting x val
    matB[:,1] = matB[:,1] * ca + matB[:,0] * sa # rotation y
    matB[:,0] = tmp
    matB[:] += matA[:,0:2] # translate back
    return matB


pygame.init()

#set up the display
size = (600,600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Arrow Field")

for i in range(20):
  for j in range(20):
    add_arrow(30*i+10, 30*j+10, 20)

np_arrows = np.array(arrows)

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
  draw_arrows()

  #Limit to 60 frames per second
  #clock.tick(30)

  # Go ahead and update the screen with what we've drawn.
  pygame.display.update()

#Close the window and quit
pygame.quit()
