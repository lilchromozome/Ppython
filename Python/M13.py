# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:09:58 2022

@author: willi
"""
import math

def factorialR(n):
    if n == 0:    
        return 1
    else:
        return n * factorialR(n-1)
    

def mystery(value, low = 1, high = None):
    if value < 1: raise Exception("Error: value < 1")
    if low < 1: raise Exception("Error: low < 1")
    if high is None: high = value

    guess = (high - low) / 2 + low        
    if math.isclose(guess**2, value):
        return guess            
    elif guess**2 > value:
        return mystery(value, low, guess)            
    else:
        return mystery(value, guess, high)
    
def fibo(n):
    vals = {1:1, 2:1}
    nums = []
    for i in range(n):
        nums.append(vals[i+1])
        try: vals[i+2]
        except: vals[i+2] = vals[i]+vals[i+1]
    return nums

def fibor(n, nums = []):
    if n <= 1:
        return n
    else:
        a = (fibor(n-1) + fibor(n-2))
        return a
    return nums

if __name__ == '__main__':
    print(mystery(10))
    print(fibor(5))