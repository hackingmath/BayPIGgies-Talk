'''wolfram pyramid
4/4/16'''

import numpy
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

x = -30
y = 7
z = 54

x,y,z = mc.player.getPos()
tableSize = 101

def neighbors(listA,r,c):
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
    
def wolfram(level):
    '''returns the array for level'''
    tableSize = 101
    surface = numpy.zeros((tableSize,tableSize))
    surface[int(tableSize/2)][int(tableSize/2)] = 1
    
    for i in range(level):
        newSurface = []
        for r in range(len(surface)):
            newSurface.append([])
            for c in range(len(surface[r])):
                if neighbors(surface,r,c) in [1,4] or surface[r][c] == 1:
                    newSurface[r].append(1)
                else:
                    newSurface[r].append(0)
        surface = newSurface
    return surface

mc.setBlocks(x,y,z,x+200,y+200,z+200,0)
cubeList = [] #list for storing cubes

#loop over each level:
for i in range(50,-1,-1):
    rowList = wolfram(i)
    for row,value in enumerate(rowList):
        for j,v in enumerate(value):
            if v == 1:
                mc.setBlock(x+row,
                            y+50-i,
                            z+j,82)


				
	    
