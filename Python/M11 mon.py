# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:59:10 2022

@author: willi
"""
import numpy as np 
import math as m
# a = np.arange(1,49).reshape(3,4,4)
# print(a)

# print(f'A: {a[1,0,3]}')
# print(f'B: {a[0,2]}')
# print(f'C: {a[2]}')
# print('D:')
# print(a[...,1,0:2])

# print('E:')
# print(a[2,:,3:1:-1])

# print('F:')
# print(a[:,::-1,0])

# print('G')
# print(np.array(([a[0,0,0], a[0,0,3]], [a[2,3,0], a[2,3,3]])))

# L = 1
# nval = np.linspace(1,5,5)
# xval = np.linspace(0,1,101)

# n, x = np.meshgrid(nval,xval)
# lam = 2 * L/n
# f = x * (L-x) * np.sin(2 * np.pi * x / lam)

# print(f)
# print(f.argmin(axis = 0))
# print(f.argmax(axis = 0))


M = np.array([[2,3,-15], [-5, 7, 22], [11,0,3]])
N = np.array([[1,7,5], [-2,8,-6], [9,-4,3]])

# print(M)
# print(N)

# elprod = M * N
# maprod = M @ N

# # print('\n' , elprod)
# # print(maprod)

# # print(np.linalg.inv(M))

# A = np.array([[3,1,-1], [8,0,3], [2, -5, -4]])
# B = (([25],[41],[39]))
# # invA = np.linalg.inv(A)
# # sol = A@B
# # print('\n', sol)
# print(np.linalg.solve(A,B))

# C = np.arange(0,16).reshape(4,4)

# print(np.linalg.det(C))

# for n in np.diff(C.all()): 
#     if n.all() == 1: print(True)

shape = np.array([[0,0], [2,5], [5,5], [7,0], [5,-5], [2, -5], [0,0]])
# s1 = shape[:len(shape)-1,0, ...] @ shape[1:,1,...]
# s2 = shape[:len(shape)-1,1, ...] @ shape[1:,0,...]
# print(0.5 * abs(s1-s2))

np.append(shape, [1,1])
print(shape)



