'''Dynamic Fractal Trees
adapted From How to Think Like a Computer Scientist
http://openbookproject.net/thinkcs/python/english3e/recursion.html '''

import pygame
from math import sin, cos,pi,radians
from pygame.locals import *

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
VIOLET = (148,0,211)

HEIGHT = 600
WIDTH = 600
size = (WIDTH,HEIGHT)
#ratio of branch to trunk:
ratio = 0.75
#angle of offset:
angle = radians(0)

#set up display
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Fractal Tree')

clock = pygame.time.Clock()

#define your functions:

def tree(position,tlength,level,angle, heading):

    newposition = (position[0] + tlength*ratio*cos(heading),
                   position[1] + tlength*ratio*sin(heading))

    pygame.draw.line(screen,VIOLET,position,newposition,level)

    if level > 0:
        tree(newposition,tlength*ratio,level-1,angle,heading+angle)
        tree(newposition,tlength*ratio,level-1,angle,heading-angle)
        

#loop until user clicks the close button
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT: #if pygame window is closed by user
            done = True

    #fill the screen with background color
    screen.fill(WHITE)

    #draw here
    position = (WIDTH//2,HEIGHT-50)
    tree(position,0.3*HEIGHT,8,angle,radians(-90))

    #increment angle
    angle += radians(1)
    #update the screen
    pygame.display.update()
    clock.tick(60)

#quit and close
pygame.quit()
