from turtle import *

def sierpinski(side_length, level):
    speed(0)
    color('orange')
    if level == 0: return
    begin_fill()
    for i in range(3):
        sierpinski(side_length/2,level - 1)
        fd(side_length)
        rt(120)
    end_fill()

seth(60)
sierpinski(200,6)
