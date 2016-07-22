"""
 Pascal's Triangle to Sierpinski
 Template from Prof. Craven
 http://simpson.edu/computer-science/
"""
 
import pygame
import operator as op
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
VIOLET = (148,0,211)
CYAN = (0,255,255)

HEIGHT = 500
WIDTH = 750

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def triangle(x,y,size,filled):
    '''draw an equilateral triangle'''
    #if the number isn't a multiple of 2, color it in.
    if filled % 8 != 0: 
        pygame.draw.polygon(screen,VIOLET,[[x,y],
                                       [x-size/2.,y+1.732*size/2.],
                                       [x+size/2.,y+1.732*size/2.]],
                                        0)
        
    else: thick = 0 #leave multiples of 2 empty

def gasket(rows):
    '''draws a sierpinski Gasket of a given number of rows'''
    size = 500./rows #resize depending on the number of rows
    for i in range(rows):
        for j in range(i+1):
            y = 1.732*i*size/2. #height of equilateral triangle
            x = -i*size/2. + j * size + WIDTH/2. #width of triangle
            triangle(x,y,size,ncr(i,j)) #draw the triangle
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

#variable for number of rows:
numberOfRows = 2
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                numberOfRows -= 1
            if event.key == pygame.K_UP:
                numberOfRows += 1
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    gasket(numberOfRows)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
