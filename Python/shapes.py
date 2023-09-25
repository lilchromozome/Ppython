# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:00:15 2022

@author: willi
"""
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, point, radius):
        self.radius = radius
        self.centerX = point.x
        self.centerY = point.y
               
    def setX(self, x):
        self.centerX = x
        
    def setY(self, y):
        self.centerY = y
        
    def getX(self):
        return self.centerX
    
    def getY(self):
        return self.centerY
    
    def getPerimeter(self):
        return math.pi * 2 * self.radius
    
    def getArea(self):
        return math.pi * self.radius**2
    
    def contains(self, other):
        d = (self.getX() - other.getX())**2 +  (self.getY() - other.getY())**2
        if math.sqrt(d) <= self.radius + other.radius:
            return True
        else: return False
        
if __name__ == "__main__":
    p1 = Point(0,0)
    c1 = Circle(p1, 2)
    p2 = Point(1,2)
    c2 = Circle(p2, 3)
    
    print(Circle.getX(c1))
    print(Circle.getPerimeter(c1))
    print(Circle.contains(c1,c2))
        
        
        
        
