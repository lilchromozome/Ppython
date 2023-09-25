# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:43:43 2022

@author: willi
"""
import math

#F = 1.8C+32
#K = C + 273.15

def C2F(c):
    return 1.8*c + 32

def F2C(f):
    return (f-32)/1.8

def C2K(c):
    return c+273.15

def K2C(k):
    return k-273.15

def K2F(k):
    return C2F(K2C(k))

def F2K(f):
    return C2K(F2C(f))

# def findnums(str):
#     while str[count].isdigit() or str[count] == '.':
        
#     return float(newstr)
        

# if __name__ == "__main__":
#     temp = input('Enter temperature')
#     if temp.find(C) >= 0:
#         print 