'''Wolfram CA
Zoomable
Scrolls slowly!'''

import pygame
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

#CA variables
w = 2
rows = 1000
cols = 1000
ruleset = [0,0,0,1,1,1,1,0] # Rule 30

cells = []
for r in range(rows):
    cells.append([])
    for c in range(cols):
        cells[r].append(0)
cells[0][cols//2] = 1

def rules(a,b,c):
    return ruleset[7-(4*a+2*b+c)]

def generate():
    for i,row in enumerate(cells): #look at first row
        for j in range(1,len(row)-1):
            left = row[j-1]
            me = row[j]
            right = row[j+1]
            if i < len(cells) - 1:
                cells[i+1][j] = rules(left,me,right)
    return cells

def newgen():
    '''Add new row to bottom of cells array'''
    #cells.remove(cells[0]) #delete top row
    newrow = []
    for i in cells[-1]:
        for j in range(1,len(cells[-1])-1):
            left = cells[-1][j-1]
            me = cells[-1][j]
            right = cells[-1][j+1]
            newrow.append(rules(left,me,right))
    return newrow

cells = generate()
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
            elif event.key == K_DOWN: w -=1

    #fill the screen with background color
    screen.fill(BLACK)

    #cells = generate()
    newrow = newgen()
    cells.remove(cells[0])
    cells.append(newrow)

    #draw here
    for i,cell in enumerate(cells): #rows
        for j,v in enumerate(cell): #columns
            if v == 1:
                pygame.draw.rect(screen,RED,[j*w-(cols*w-WIDTH)/2,
                                             w*i,w,w])
    

    #update the screen
    pygame.display.update()

    clock.tick(60)
    
#quit and close
pygame.quit()
