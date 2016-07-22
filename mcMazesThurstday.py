'''Amazing Mazes!'''

from mcpi import minecraft
mc = minecraft.Minecraft.create()

#get the location of player
x,y,z = mc.player.getTilePos()

m = [[1,0,1,1,0,1,1,1],
     [1,0,0,1,0,0,0,1],
     [1,1,0,1,1,1,0,1],
     [1,0,0,1,1,1,0,1],
     [1,0,1,1,1,1,0,1],
     [1,0,0,0,1,0,0,1],
     [1,1,1,0,1,1,1,1],
     [1,1,1,0,1,1,1,1]]

for j,u in enumerate(m):
    for i,v in enumerate(u): #loop through the elements in list m
        if v == 1: #if there's a 1 
            mc.setBlocks(x+j,y,z + i,
                         x+j,y+3,z+i,57) #set a block
