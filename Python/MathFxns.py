# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:17:21 2022

@author: willi
"""

def multiples(n, x = 1, y = 1):
    num_multiples = int((n-1)/x)
    sumx = x*num_multiples*(num_multiples+1)/2
    num_multiples = int((n-1)/y)
    sumy = y*num_multiples*(num_multiples+1)/2
    return sumx + sumy

def fibo(n):
    num1 = 1
    num2 = 1
    print(num1, end=', ')
    for count in range(n-1):
        sum = num1+num2
        num1 = num2
        num2  = sum
        print(num1, end=', ')
    return

def fiboEven(n):
    num1 = 1
    num2 = 1
    for count in range(n-1):
        sum = num1+num2
        num1 = num2
        num2  = sum
        if num1%2 == 0: print(num1, end=', ')
    return

    
if __name__ == "__main__":
    #print(multiples(305,3,5))
    print(fibo(400))
    #print(fiboEven(90))




    
    
    
    # def fibor(n):
    #     if n <= 1:
    #         return n
    #     else:
    #         x = (fibor(n-1) + fibor(n-2))
    #     print(x, end=', ')
    #     return x
    
