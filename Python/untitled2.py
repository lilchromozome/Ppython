# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:30:43 2022

@author: willi
"""
from graphics import *
import time
import math

g = 9.8
radius = float(input("Enter radius 10-20 "))                     #get inputs
v0 = float(input("Enter initial velocity 30-80 "))
theta = float(input("Enter launch angle 10-90 ")) *math.pi / 180
dt = float(input("Enter time increment 0.01 - 0.5 "))

H = v0**2 / (2 * g) * math.sin(theta)**2          #window size
R = v0**2 / g * math.sin(2*theta)

x_axis = math.floor(2 * (R + (3 * radius)))           ##/when sin theta, v0 big & rad is small, offscreen
y_axis = math.floor(H + (3 * radius))

#Create graphics window with appropriate size
win = GraphWin ( 'Trajectory ', x_axis , y_axis)
# Put ball at bottom left
p1 = Point (radius , math.floor(H + 2*radius))          #small radius looks too right but because window can't be smaller

# win = GraphWin ( 'Trajectory ', 700 , 300)
# # Put ball at bottom left
# p1 = Point (radius , 300-radius)

# Create circle
C = Circle (p1 , radius )

C.setFill("yellow")                                        # Draw circle
C.draw(win) 
time.sleep(1) # Wait 1 second
# print the x and y coordinates of the center of the c i r c l e
print(f'Circle center x coordinates : {C. getCenter ( ) . getX ()}')
print(f'Circle center y coordinates : {C. getCenter ( ) . getY ()}')

def bounce(v):                                                                      #method to bounce the ball
    for step in range(steps):
        dx = (v * math.cos(theta) * dt)
        dy = ((v * math.sin(theta)) - g * step * dt) * -dt
        if C.getCenter().getX() != radius and C.getCenter().getY() + radius + dy >= y_axis:      #correction if ball goes under
            dy_correct = -(radius + C.getCenter().getY() - y_axis)
            dx_correct = dx * dy_correct/dy
            C.move(dx_correct, dy_correct)
            print(f'interation: {step} , dx = {dx:.3f} , dy = {dy:.3f}')
            break
        else:
            C.move(dx,dy)
            time.sleep(0.01)
            print(f'interation: {step} , dx = {dx:.3f} , dy = {dy:.3f}')
    print(C.getCenter())

if __name__ == "__main__":                              # executed code
    T = 2 * v0 * math.sin(theta) / g
    steps = math.ceil(T / dt)
    dx = (v0 * math.cos(theta) * dt)
    dy = (v0 * math.sin(theta)) * dt
    while int(dy) > 0:
        bounce(v0)
        v0 = v0 * .56
        dy = (v0 * math.sin(theta)) * dt
    
    

""" DO NOT MODIFY OR WRITE ANYTHING BELOW """

try:
    win.getMouse()    
    win.close()
except:
    pass