"""
 Pascal's Triangle to Sierpinski
 Template from Prof. Craven
 http://simpson.edu/computer-science/
"""
 
import pygame
 
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
    
def factorial(x):
    if x == 0: return 1
    return x*factorial(x-1)

def combin(r,k):
    return int(factorial(r)/(factorial(k)*factorial(r-k)))

def triangle(x,y,size,filled):
    '''draw an equilateral triangle'''
    #if the number isn't a multiple of 2, color it in.
    if filled % 8 != 0: 
        pygame.draw.polygon(screen,CYAN,[[x,y],
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
            triangle(x,y,size,combin(i,j)) #draw the triangle
            #display text
            font = pygame.font.Font(None,int(200/rows))
            text = font.render(str(combin(i,j)), True, BLACK)
            screen.blit(text,[x,y+1.732*size/4])
            
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

#fill Background:
#background = pygame.Surface(screen.get_size())
#background = background.convert()
#background.fill((255,255,255)) #white
 
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
