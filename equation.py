from __future__ import division
from math import sqrt
import cmath

def equation(a,b,c,d):
    '''Solves equations of the
    type ax + b = cx + d'''
    return (d - b)/(a - c)
    
def pythag(leg1,leg2):
    '''solves for hypotenuse c
    of right triangle'''
    return sqrt(leg1**2 + leg2**2)

def pythag2(leg1,hyp):
    '''solves for other leg
    of right triangle'''
    return sqrt(hyp**2 - leg1**2)


def synthdiv(divisor,dividend):
    '''divides a polynomial by a constant
    and returns a lower-degree polynomial.
    Enter divisor as a constant: (x - 3) is 3
    Enter dividend as a list of coefficients, like [1,5,6]'''
    quotient = []
    row2 = [0]
    for i in range(len(dividend)):
        quotient.append(dividend[i]+row2[i])
        row2.append(divisor*quotient[i])
    print quotient

def factors(n):
    '''returns a list of factors of n'''
    factor_list = [1.0]
    for i in range(2,n+1):
        if n % i == 0:
            factor_list.append(float(i))
    return factor_list

def f(x):
    #return 6*x**3 + 31*x**2 + 3*x - 10
    #return 48*x**5 - 44*x**4 - 884*x**3 + 321*x**2 + 3143*x +980
    #return 40*x**5 - 158*x**4 - 1781*x**3 + 2392*x**2 + 11839*x + 520
    #return 0.1*x**6-2.7*x**5+12*x**4+2.2*x**3-50*x**2-4*x+3.7
    return 1.6*x**5 + 3.9*x**4 -1.9*x**3 - 5.0*x**2+.4*x+0.5

def plug(factorList):
    for x in factorList:
        if round(f(x),6) == 0:
            print "One solution is",x
    print "Finished plugging."

def rational_roots(a,b):
    '''Returns all possible rational roots of
    a polynomail with first coefficient a and
    constant b'''
    roots = []
    numerators = factors(b)
    denominators = factors(a)
    for numerator in numerators:
        for denominator in denominators:
            roots.append(numerator / denominator)
            roots.append(-numerator / denominator)
    return roots

def synth_div(divisor, dividend):
    '''divides a polynomial by a constant
    and returns a lower-degree polynomial
    Enter divisor as a constant: (x-3) is 3
    Enter dividend as a list of coefficients:
    x**2 - 5*x + 6 would be [1,-5,6]'''
    quotient = []
    row2 = [0]
    for i in range(len(dividend)):
        quotient.append(dividend[i] + row2[i])
        row2.append(divisor*quotient[i])
    print quotient

def quad(a,b,c):
    '''returns the solutions of equations of the
    form ax^2 + bx + c = 0 using the quadratic
    formula.'''
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return [x1,x2]

def quad2(a,b,c):
    '''returns solutions of equations of the form
    a*x**2 + b*x + c = 0'''
    discriminant = b**2 - 4*a*c
    if discriminant >= 0: #real solutions
        x1 = (-b + sqrt(discriminant))/(2*a)
        x2 = (-b - sqrt(discriminant))/(2*a)
        return [x1,x2]
    else: #imaginary solutions
        real_part = -b/(2*a)
        imaginary_part = sqrt(-discriminant)/(2*a)
        x1 = real_part+imaginary_part*cmath.sqrt(-1)
        x2 = real_part+imaginary_part*round(cmath.sqrt(-1),2)
        return [x1,x2]

def derivative(x):
    '''gives the derivative of f at x'''
    deltax = 1./1000000
    return (f(x + deltax) - f(x))/deltax

def newton(guess):
    '''uses Newton's method to find the roots of
    a function with "guess" as the first input.'''
    for i in range(30):
        new_guess = guess - f(guess)/derivative(guess)
        guess = new_guess
    return new_guess

#plug(rational_roots(40,520))
    
def newton_solve():
    '''returns a list of the roots of f(x) by plugging in guesses
    between -50 and 50.'''
    root_list = []
    x = -50
    while x < 50:
        root1 = round(newton(x),6) #round off to two decimal places
        if root1 not in root_list: #check if that root is in the list
            root_list.append(root1) #already. If not, add to list.
        x += 0.5 	#next "guess"
    return root_list

    
#print(newton_solve())
