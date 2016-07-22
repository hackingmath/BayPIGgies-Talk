from __future__ import division

'''Fireworks!'''

#From Harbour "More Python Programming..."
#template for pygame projects

#import modules
import pygame
from pygame.locals import *
from math import pi, sin, cos,radians
from random import randint,choice,uniform
import numpy as np

class Particle:
    def __init__(self,x,y,angle,vel,red,green,blue):
        self.x = x
        self.y = y
        self.dx = vel * cos(angle)
        self.dy = vel * sin(angle)
        self.red = red
        self.green = green
        self.blue = blue
        self.lifespan = 255

    def update(self,listA):
        self.dy += fgrav
        self.x += self.dx
        self.y += self.dy
        self.lifespan -= 0.5
        if self.y > HEIGHT or self.lifespan == 0:
            listA.remove(self)
        pygame.draw.ellipse(screen,(self.lifespan*self.red,
                                        self.lifespan*self.green,
                                        self.lifespan*self.blue),
                            [self.x,self.y,10,10])

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
VIOLET = (148,0,211)
CYAN = (0,255,255)
fgrav = 0.125 #acceleration due to gravity
colors = (RED, WHITE, BLUE)
particle_list = []

#set display constants

WIDTH = 600
HEIGHT = 600
size = (WIDTH,HEIGHT)


#set up display
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Fireworks!')


#loop until the user clicks the close button
done = False

while done == False:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            done = True
        if event.type == MOUSEBUTTONDOWN:
            mouseX,mouseY = pygame.mouse.get_pos()
            thecolor = choice(colors)
            if thecolor == RED:
                red = 1
                green = 0
                blue = 0
            elif thecolor == WHITE:
                red = 1
                green = 1
                blue = 1
            else:
                red = 0
                green = 0
                blue = 1
            for i in range(400):
                particle_list.append(Particle(mouseX,
                                              mouseY,
                                              uniform(0,6.28),
                                              uniform(0,10),
                                              red,
                                              green,
                                              blue))
    
    
    #fill the screen
    screen.fill(BLACK)

    #draw your items
    for p in particle_list:
        p.update(particle_list)

    pygame.display.update()

#Quit nicely
pygame.quit()
    
