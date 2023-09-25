# -*- coding: utf-8 -*-
"""
Template code


1) Get the user inputs
2) Generate a window with the appropriate size based on the user inputs
3) Place the initial circle (ball) in the window as described in the instruction
4) Run the simulation and check when the ball hits the horizontal edge. Make the necessary adjustment
5) Termiunate the simulation when the stopping criteria is reached.



"""

from graphics import *
import time
import math




""" Write your code here """
g = 9.8
#get inputs
radius = float(input("Enter radius 10-20 "))                     
v0 = float(input("Enter initial velocity 30-80 "))
theta = float(input("Enter launch angle 10-90 ")) * math.pi / 180
dt = float(input("Enter time increment 0.1 - 0.5 "))

# correct window size
H = v0**2 / (2 * g) * math.pow(math.sin(theta) ,  2)                     
R = v0**2 / g * math.sin(2 * theta)
x_axis = math.floor(2 * (R + 3 * radius))
y_axis = math.floor(H + 3 * radius)

#Create graphics window with appropriate size
win = GraphWin ( 'Trajectory ', x_axis , y_axis)
# Put ball at bottom left
p1 = Point (radius , math.floor(H + 2*radius))

# Create yellow circle
C = Circle (p1 , radius )
C.setFill("yellow")                                        
C.draw(win)
 
time.sleep(1)                                               

#method to bounce the ball
def bounce(v):                                                                      
    for step in range(2 * steps):
        dx = (v * math.cos(theta) * dt)
        dy = ((v * math.sin(theta)) - g * step * dt) * -dt
        #correction if ball goes under horizontal axis
        if C.getCenter().getX() != radius and C.getCenter().getY() + radius + dy >= y_axis:      
            dy_correct = -(radius + C.getCenter().getY() - y_axis)
            dx_correct = dx * dy_correct/dy
            C.move(dx_correct, dy_correct)
            #print iteration and speeds
            print(f'interation: {step:3} , dx = {dx:6.3f} , dy = {-dy:6.3f}')                
            break
        #ball flight when in open air
        else:                                               
            C.move(dx,dy)
            time.sleep(0.05)
            #print iteration and speed
            print(f'interation: {step:3} , dx = {dx:6.3f} , dy = {-dy:6.3f}')        


# executed code
if __name__ == "__main__":
    #Initial values for ball flight variables                              
    T = 2 * v0 * math.sin(theta) / g
    steps = math.ceil(T / dt)
    dx = (v0 * math.cos(theta) * dt)
    dy = (v0 * math.sin(theta)) * dt
    #loop for consecutive bounces
    while int(dy) > 0:
        T = 2 * v0 * math.sin(theta) / g
        steps = math.ceil(T / dt)
        bounce(v0)
        v0 = v0 * .56
        dy = (v0 * math.sin(theta)) * dt


""" DO NOT MODIFY OR WRITE ANYTHING BELOW """

# Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass
    
