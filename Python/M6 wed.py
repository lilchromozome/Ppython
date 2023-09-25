# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:09:07 2022

@author: willi
"""
import math

myFriends = {'Amanda', 'Bobby', 'Cathy', 'Dave', 'Ellen'}
yourFriends = {'Adam', 'Brent', 'Cathy', 'Daniel', 'Ellen'}

def mutualFriends(f1, f2):
    l = list(f1.intersection(f2))
    l.sort()
    return l

def ourFriends(f1,f2):
    l = list(f1.union(f2))
    l.sort()
    return l

def theirFriends(f1, f2):
    l = list(f2.difference(f1))
    l.sort()
    return l

def primes(n):
    nums = []
    for num in range(1, n+1):
        nums.append(num)
    for div in range(2, math.ceil(n/2)):
        for m in nums:
            if int(m/div) > 1 and m%div == 0:
                nums.remove(m)
    return nums

def getAge():
    age = input('Enter Age:')
    try:
        age = float(age)
        print(f'You are {age} years young!')
    except ValueError: print('invalid age')
    
    
def squareInteger():
    num = input('Enter positive integer:')
    try:
        if int(num) < 0:
            raise ValueError
        print(int(num)**2)
    except ValueError: print('Not a positive integer')
    pass


if __name__ == "__main__":
    squareInteger()
    
    