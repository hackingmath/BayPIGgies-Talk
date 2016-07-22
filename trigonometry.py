'''All the code from the Trigonometry Chapter
of Hacking Math Class'''
from turtle import *
from math import pi, sin, cos, e, sqrt, acos

def harmonograph():
    '''Creates graphics from oscillations.'''

    #frequencies
    f1 = 2
    f2 = 6
    f3 = 1.002
    f4 = 3

    #phase shifts
    p1 = pi/16
    p2 = 3*pi/16
    p3 = 13*pi/16
    p4 = pi

    #decay constants:
    d1 = 0.02
    d2 = .0315
    d3 = .02
    d4 = 0.02

    t = 0
    dt = 0.1

    clear()
    color("red")

    for i in range(5000):
        speed(0)
        x1 = 100*sin(f1*t + p1)*e**(-t*d1) + 100*sin(f2*t + p2)*e**(-t*d2)
        y1 = 100*sin(f3*t + p3)*e**(-t*d3) + 100*sin(f4*t + p4)*e**(-t*d4)
        setpos(x1,y1)
        t += dt


def convToRads(degrees):
    '''converts degrees to radians'''
    return degrees*pi/180

def convToDegs(radians):
    '''Converts radians to degrees'''
    return radians*180/pi

def lawofCos_c(a,b,C):
    '''Returns the side opposite the given angle in
    a triangle using the Law of Cosines
    Enter side, side, angle'''
    c = sqrt(a**2 + b**2 - 2*a*b*cos(convToRads(C)))
    return c

def lawofCos_C(a,b,c):
    '''Returns the angle opposite side c in
    a triangle using the Law of Cosines
    Enter 3 sides'''
    C = convToDegs(acos((c**2 - a**2 - b**2)/(-2*a*b)))
    return C

def solveTri3sides(a,b,c):
    '''Solves for all three sides and all three angles in a
    triangle using the Law of Cosines
    given 3 sides'''
    C = lawofCos_C(a,b,c)
    A = lawofCos_C(b,c,a)
    B = 180 - C - A
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
    print("A = ",A)
    print("B = ",B)
    print("C = ",C)
