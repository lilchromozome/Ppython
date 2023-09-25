# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:30:22 2022

@author: willi
"""
import tempConversion
import math

def isPrime(n):
    prime = True
    for count in range(2,int(n/2+1)):
        if n%count == 0:
           prime = False 
    return prime
  
def gauss(x, mu=0, sigma=1):
    pt1 = 1/(sigma * math.sqrt(math.pi * 2))
    pt2 = math.pow(math.e,-1/2*math.pow((x-mu)/sigma,2))
    return pt1*pt2      
    
def repeater(str, end, rpt):
    repeat = str[:end]
    out = ''
    for num in range(rpt):
        out = out + repeat
    return out

def isPalindrome(num):
    string = str(num)
    palin = False
    if string[-1::-1] == string:
        palin = True
    return palin

def riddle():
    for num in range (1000000):
        string = str(num)
        if isPalindrome(string[2:6]):
            string = str(num+1)
            if isPalindrome(string[1:6]): 
                string = str(num+2)
                if isPalindrome(string[1:5]):
                    string = str(num+3)
                    if isPalindrome(string):
                        print(f'{num:06d}')

#_  _    n m m n
#_   n+1 n m m n+1
#_   n+1 n m n+1 n+2
#n+3 n+1 n m n+1 n+3




if __name__ == "__main__":



                
    # a = float(input('Enter x'))
    # b = float(input('Enter mu'))
    # c = float(input('Enter sigma'))
    # print(f'{gauss(a,b,c):.3f}')
    
    # num = int(input('Enter an integer'))
    # if isPrime(num) == True:
    #     print('This integer is prime')
    # else:
    #     print('This integer is not prime')    
    # print(f'{tempConversion.F2C(72):.2f}')
    # print(repeater('computer',4,6))
    riddle()