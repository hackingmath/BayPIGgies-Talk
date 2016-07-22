'''The fractal chapter from
Hacking Math Class'''

from turtle import *
import random
import operator as op
from functools import reduce
speed(0)

def y(length,level):
    if level > 0:
        fd(length)
        lt(40)
        y(length*0.8,level-1)
        rt(60)
        y(length*0.9,level-1)
        lt(20)
        bk(length)

goto(0,-300)
clear()
seth(90)
y(100,8)

def square(length):
    '''square starts from bottom left corner.'''
    color('purple')
    begin_fill() #fills the shape with color
    for i in range(4):
        fd(length)
        rt(90)
    end_fill()  
  
def tree(length,level):
    speed(0)
    if level == 0:
        return
    pu()
    fd(length/2)
    pd()
    lt(90)
    fd(length/2)
    rt(90)
    square(length) # the big square
    fd(length)
    rt(90)
    fd(length/2)
    lt(135)
    tree(length/(2**0.5),level-1) # the left square
    rt(90)
    tree(length/(2**0.5),level-1) # the right square
    pd()
    rt(45)
    fd(length/2)
    rt(90)
    fd(length)
    rt(90)
    fd(length/2)
    rt(90)
    pu()
    bk(length/2)
    
'''setpos(0,-300)
clear()
seth(90) #face upwards
tree(150,5)'''

def side(length,level):
    if level == 0:
        fd(length)
        return
    side(length/3, level - 1)
    lt(60)
    side(length/3, level - 1)
    rt(120)
    side(length/3, level - 1)
    lt(60)
    side(length/3,level - 1)

def side2(length,level):
    '''alternative option to "side"'''
    if level == 0:
        fd(length)
        return
    side(length/3, level - 1)
    rt(60)
    side(length/3, level - 1)
    lt(120)
    side(length/3, level - 1)
    rt(60)
    side(length/3,level - 1)

def snowflake(length,level):
    pd()
    speed(0)
    for i in range(3):
        '''if random.random()<0.5:
            side2(length,level)'''
        side(length,level)
        rt(120)

#snowflake(300,4)

def sierpinski(side_length, level):
    speed(0)
    if level == 0:
        return
    begin_fill()
    for i in range(3):
        sierpinski(side_length/2, level-1)
        fd(side_length)
        lt(120)
    end_fill()

#sierpinski(300,5)

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

def pascal(rows):
    for row in range(rows):
        for col in range(row+1):
            print(ncr(row,col),' ',end='')
        print()

#pascal(7)
exitonclick()
