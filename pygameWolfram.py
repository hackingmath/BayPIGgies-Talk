'''Wolfram Automata'''

import pygame
from pygame.locals import *
import numpy

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
VIOLET = (148,0,211)

WIDTH = 600
size = (WIDTH,WIDTH)
tableSize = 101
scale_factor = WIDTH/tableSize

def neighbors(listA,r,c):
    '''puts 4 neighbors of a cell into a list'''
    neighborList = []
    neighborList.append(listA[r-1][c])
    neighborList.append(listA[r][c-1])
    neighborList.append(listA[r][c+1])
    neighborList.append(listA[r+1][c])
    #count the 1's in the list
    return neighborList.count(1)

def nbs(listA,r,c):
    '''puts 4 neighbors of a cell into a list'''
    neighborList = []
    try:
        neighborList.append(listA[r-1][c])
        neighborList.append(listA[r][c-1])
        neighborList.append(listA[r][c+1])
        neighborList.append(listA[r+1][c])
        
    except IndexError:
        pass
    return neighborList.count(1)

def drawGrid(listA):
    '''draws the grid'''
    for rowind,row in enumerate(listA):
        for colind,col in enumerate(row):
            if col == 1:
                pygame.draw.rect(screen,VIOLET,[rowind*scale_factor,
                                                colind*scale_factor,
                                                scale_factor,
                                                scale_factor])
    
def wolfram(level):
    '''returns the array for level'''
    surface = numpy.zeros((tableSize,tableSize))
    surface[int(tableSize/2)][int(tableSize/2)] = 1
    
    for i in range(level): #repeat for each level
        newSurface = []     #empty list for next level
        for r,u in enumerate(surface): # for each row in array
            newSurface.append([]) #empty list in next level
            for c,v in enumerate(u): # for every item in row
                #if it has exactly 1 or 4 neighbors that are 1's
                if nbs(surface,r,c) in [1,4] or v == 1:
                    newSurface[r].append(1) #put a 1 in next level
                else: #otherwise
                    newSurface[r].append(0) #put a 0 in next level
        #replace the old level with new one for next loop
        surface = newSurface
        drawGrid(surface)
    return numpy.array(surface)

#set up display
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cellular Automata!')
clock = pygame.time.Clock()
#loop until user clicks the close button
done = False

t = 0

while not done:
    for event in pygame.event.get():
        if event.type == QUIT: #if pygame window is closed by user
            done = True

    #fill the screen with background color
    screen.fill(WHITE)

    #draw here
    wolfram(t)
    t += 1
    if t == 50:
        t = 0


    #update the screen
    pygame.display.update()

    clock.tick(120)

#quit and close
pygame.quit()
