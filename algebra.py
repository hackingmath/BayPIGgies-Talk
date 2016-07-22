'''All the code from the Hacking Math Class Book
Chapter 2: Algebra'''

from turtle import *
from math import sqrt
#from arithmetic import factors

def equation(a,b,c,d):
    '''Returns the solution of an equation
    of the form ax + b = cx + d'''
    return (d - b)/(a - c)
    
#To solve -4x + 5 = 0.25x - 0.3
#print("x = ",equation(-4,5,0.25,-.3))

def pythag(leg1,leg2):
    '''solves for hypotenuse'''
    return sqrt(leg1**2 + leg2**2)

def pythag2(leg1,hyp):
    '''solves for other leg
    of right triangle'''
    return sqrt(hyp**2 - leg1**2)

def quad(a,b,c):
    '''Returns the solution of an equation
    of the form ax + b = cx + d''' 
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print(x1, ',', x2)

#To solve 2*x**2 + 7*x - 11 = 0:    
#quad(2,7,-11)

def quad2(a,b,c):
    '''returns solutions of equations of the
    form a*x**2 + b*x + c = 0'''
    discriminant = b**2 - 4*a*c
    if discriminant >= 0: #real solutions
        x1 = (-b + sqrt(discriminant))/(2*a)
        x2 = (-b - sqrt(discriminant))/(2*a)
        print(x1,",", x2)
    else: #imaginary solutions
        real_part = -b/(2*a)
        imaginary_part = sqrt(-discriminant)/(2*a)
        print(real_part,"+",str(imaginary_part)+"i")
        print(real_part,"-",str(imaginary_part)+"i")


def plug():
    for x in rational_roots(48,980):
        if 48*x**5 - 44*x**4 - 884*x**3 + 321*x**2 + 3143*x +980 == 0:
            print("One solution is", x)
    print("Done plugging.")

def setupOLD():
    speed(0) 	    #Sets turtle speed to fastest
    setworldcoordinates(-5,-5,5,5) #lower left and upper right corners
    setpos(0,0)     #sets turtle's position to (0,0)
    clear()         #Clears its trails
    setheading(0)   #Faces the right of the screen
    pd()            #Puts its pen down to draw
    color("black")  #Sets its color to black    
    for i in range(4):  #"Do this four times"
        setpos(0,0)     #Centers itself again
        fd(5)           #Go forward 5 steps
        rt(90)          #turn right 90 degrees
    pu()            #Sets its pen in up position

def plug2():
    for x in range(-100,100):
        if 6*x**3 + 31*x**2 + 3*x - 10 == 0:
            print("One solution is", x)
    print("Done plugging.")

def plug():
    x = -100
    while x <= 100:
        if 6*x**3 + 31*x**2 + 3*x - 10 == 0:
            print("One solution is", x)
        x += 0.5 #Will go up in half-unit steps
    print("Done plugging.")

def setup1():
    speed(0) 	    #Sets turtle speed to fastest
    setworldcoordinates(-6,-5,6,5) #lower left and upper right corners
    setpos(0,0)     #sets turtle's position to (0,0)
    clear()         #Clears its trails
    setheading(0)   #Faces the right of the screen
    pd()            #Puts its pen down to draw
    color("black")  #Sets its color to black    
    for i in range(4):  #"Do this four times"
        setpos(0,0)     #Centers itself again
        fd(5)           #Go forward 5 steps
        rt(90)          #turn right 90 degrees
    pu()            #Sets its pen in up position 

def mark():
    rt(90)
    fd(0.1)
    bk(0.2)
    fd(0.1)
    lt(90)
    
def setup():
    speed(0) #Sets turtle speed to fastest
    setworldcoordinates(-6,-5,6,5) #lower left and upper right corners
    setpos(0,0)     #sets turtle's position to (0,0)
    clear()         #Clears its trails
    setheading(0)   #Faces the right of the screen
    pd()            #Puts its pen down to draw
    color("black")  #Sets its color to black    
    for i in range(4):  #"Do this four times"
        setpos(0,0)     #Centers itself again
        for i in range(6): #Make 5 tick marks
            fd(1)       
            mark()      
        rt(90)          
    pu()            #Sets its pen in up position

def f(x):           #This defines the function f(x)
    #return 2*x + 3  #The line y = 2x + 3
    return 2*x**2+7*x-11#6*x**3 + 31*x**2+3*x-10
	#return -0.2*x**5 + 1.4*x**4+x**3-5*x**2-1.5*x + 3

def graph(f):    #The function f(x) has to be defined
    speed(0)    #Sets speed to the fastest
    color("black")  #Sets its color
    setpos(-6,f(-6))    #Sets its position to the left edge
    pd()                #pen down
    setheading(0)       #Face right
    x = xcor()	#set a variable, x, to the x-coordinate of the turtle
    while xcor() <= 6:  #Do this until the x-coordinate is more than 6
        x += 0.01       #make x go up a tiny bit
        goto(x,f(x))    #Go to the next point on the graph


setup()
graph(f)

#Returns all the possible rational roots of
#a polynomial with first coefficient a and
#constant b
def rationalRoots(a,b):
    roots = [] #create a list to store the roots
    numerators = factors(b) # generate a list of factors of b
    denominators = factors(a) # generate a list of factors of a
    for numerator in numerators: #loop through the numerator list
        for denominator in denominators: #and the denominator list
            roots.append(numerator / denominator)
            roots.append(-numerator / denominator)
    return roots

#divides a polynomial by a constant
#and returns a lower-degree polynomial
#Enter divisor as a constant (x - 3) is 3
#Enter dividend as a list of coefficients, like [1,5,6]
def synthDiv(divisor,dividend):
    quotient = []
    row2 = [0]
    for i in range(len(dividend)):
        quotient.append(dividend[i]+row2[i])
        row2.append(divisor*quotient[i])
    print(quotient)

#Returns True if a is divisible by b
def divisible(a,b):
    return a % b == 0

#Returns "True" if it's Prime
def isPrime(n):
    m = sqrt(n)
    for i in range(2,int(m) + 1): #range has to be integers
        if divisible(n,i):
            print(n,"=",i,"x",n/i)
            return
    return True
    
#isPrime(1000001)

def primeList(n):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        if isPrime(num):
            prime_list.append(num)
        num += 1
    print(prime_list)

def binary(number): #Converts decimal number to binary
    exponent = 0    #We're dealing with exponents of 2
    binary_number = 0            #The binary form of the number
    while number >= 2**exponent: #Finds the lowest power of 2
        exponent += 1            #the number is less than
    exponent -= 1
    for i in range(exponent + 1):
        if number - 2**exponent > -1: #If number contains power of 2
            binary_number += 10**exponent #Add that power of 10
            number -= 2**exponent  #Take away that power of 2 from       
                                   #number
        exponent -= 1           	  #Next lower exponent
    print(binary_number)

exitonclick()

