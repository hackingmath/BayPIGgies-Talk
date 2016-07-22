'''Wolfram CA
Zoomable with up and down arrows
Thanks to Paddy Gaunt for
his improvements'''

import pygame
from pygame.locals import *
import numpy
import time

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
size = (WIDTH, HEIGHT)

#CA variables
w = 2
rows = HEIGHT // w
cols = 1000
ruleset = numpy.array([0,0,0,1,1,1,1,0]) # Rule 30 
generation = 0

cells = numpy.zeros((rows, cols), dtype=numpy.int)
cells[0, cols // 2] = 1

def rules(a, b, c):
    ix = 7 - (4*a + 2*b + c)
    return ruleset[ix] # you can do this with a numpy array as index to numpy array

def generate(i):
    if i >= cells.shape[0]:
        cells[:-1] = cells[1:] # roll up one
        i = cells.shape[0] - 1 # set line to refresh equal to bottom one
    elif i <= 0: # only generate after first generation
        i = 1
    # do the whole line in one numpy action
    left = cells[i-1,:-2] 
    me = cells[i-1,1:-1]
    right = cells[i-1,2:]
    cells[i,1:-1] = rules(left, me, right)
    return cells

#print cells[0] works
        
#set up display
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Caption!')
clock = pygame.time.Clock()

#loop until user clicks the close button
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT: #if pygame window is closed by user
            done = True
        if event.type == KEYDOWN:
            if event.key == K_UP: w += 1
            elif event.key == K_DOWN and w > 2: w -=1

    #fill the screen with background color
    screen.fill(BLACK)

    generation += 1
    cells = generate(generation)

    #draw here
    j0 = int(cols / 2 - WIDTH / w / 2) # range of cell indices to draw centrally
    j1 = int(j0 + WIDTH / w)
    i0 = 0
    i1 = rows

    for i in range(rows): #rows
        for j in range(j0, j1): #columns
            if cells[i, j] == 1:
                pygame.draw.rect(screen, RED, [(j - j0) * w, i * w, w, w])
    
    #update the screen
    pygame.display.update()
    clock.tick(120)
    
#quit and close
pygame.quit()

