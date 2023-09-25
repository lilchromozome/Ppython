# -*- coding: utf-8 -*-

"""
Created on Wed Aug 10 12:03:20 2022

@author: willi
"""
# Make truncate a method that Round can use
# Other classes also?
# Why can I not use variables in Class?

import math
    
num = float(input("Whats your number?"))
request = str(input("Truncate or Round?"))
sigfigs = int(input("How many sigfigs boss?"))
    
negative = False
needMultiply = False
string = str(num)
log = int(math.log10(abs(num))+1)
multiplier = 0
multi = str(multiplier)
    
    #multiplier digits>sigfigs
class Rounder:    
    if log-sigfigs > 0:
        needMultiply = True
        multiplier = int(10**(log-sigfigs))
        multi = str(multiplier)
    
    if string[0] == '-':
       sigfigs += 1
       negative = True
    
    if string.index('.')<sigfigs:
       sigfigs += 1
       
    #extra Zeros
    if log == 0:
        sigfigs +=1
    
    if sigfigs>len(string):
        needMultiply = True
        multiplier = int(10**(sigfigs-len(string)))
        multi = str(multiplier)
        
        
        print(sigfigs)
        print(log)
        print (multi)

    
    #TRUNCATOR
def Truncate(a = num,b = sigfigs):
        if needMultiply:
            return(string[0:sigfigs] + multi[1:len(multi)])
        else:
            return(string[0:sigfigs])
    
    # #ROUNDER
    # def Round():
    #     if int(string[sigfigs+1]) > 5:
    #         newnum = num + 10**(log-sigfigs)
    #         Truncate(newnum, sigfigs)
    #     else:
    #         Truncate()
        # if needMultiply:
        #     print(string[0:sigfigs] + multi[1:len(multi)])
        # else:
        #     print(string[0:sigfigs])
    
    # if request == 'truncate' or 'Truncate' or 't':
    #     print(Truncate(num, sigfigs))
    # if request == "round" or "Round" or "r":
    #     Rounder()

    
