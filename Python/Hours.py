# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:05:46 2022

@author: willi
"""

class Hour:
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
        
    def getHours(self):
        return self.hours
    
    def getMins(self):
        return self.mins
    
    def setHours(self, h):
        self.hours = h
    
    def setMins(self, m):
        self.mins = m
        
    def totalMins(self):
        return int(self.hours*60 + self.mins)
        
    def __str__(self):
        string = f'{self.hours}:{self.mins:0>2}'
        return string
    
    def __add__(self, other):
        h = self.hours + other.hours
        m = self.mins + other.mins
        if m>=60:
            h += 1
            m -= 60
        return Hour(h,m)
        
    def __truediv__(self, other):
        t = self.totalMins()/int(other)
        h = int(t/60)
        m = int(t%60)
        return Hour(h,m)
    
    def __mul__(self, other):
        h = self.getHours() * int(other)
        m = self.getMins() * int(other)
        if m>=60:
            h += int(m/60)
            m = (m%60)
        return Hour(h, m)
    
if __name__ == "__main__":
    t1 = Hour(1,57)
    t2 = Hour(3, 4)
    print(t1 + t2)
    print(t1*2)
    print(t2/2)