# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:13:34 2022

@author: willi
"""

def getAge():
    age = input('Enter age')
    if isinstance(age, float or int) and age > 0:
        print(f'You are {age} years young!')
    else: raise ValueError('Invalid age')
    
def squareInteger():
    pass
    
    


if __name__=='__main__':
    getAge()