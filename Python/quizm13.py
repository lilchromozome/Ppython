# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:03:51 2022

@author: willi
"""

import numpy as np
def create1Darray(n):
    arr = np.linspace(1,n,n)
    return arr

def createTrue(n):
    arr = np.ones([n,n])
    return arr>0

def extractOdd(a):
    return a[a%2 ==1]

def convert2D(a):
    if len(a)%2 == 0:
        a = np.vstack((a[:int(len(a)/2)],a[int(len(a)/2):]))
        return(a)
    else:
        return a
        
def common(a,b):
    return np.intersect1d(a,b)

def reverse(a):
    a = a[::-1]
    return a
"""
Write your functions here.
"""

if __name__ == "__main__":
    """
    Test your code here.
    """
    q = create1Darray(8)
    b = np.array([1,2,5,5,5,5,5,5])
    print(q)
    print(createTrue(4))
    print(extractOdd(q))
    print(convert2D(q))
    print(common(q,b))
    print(reverse(b))
    