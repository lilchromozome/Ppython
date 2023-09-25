#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:14:27 2022

@author: dimitris
"""
import numpy as np
import math
from plot_nano import *
from misc import include_atoms_gr,  grid_pq
sq3 = np.sqrt(3)

def Graphene(n, m ,l):
    '''
    A method that uses methods in the CarbonFiller class to construct
    a graphene sheet
    Input:
        n = the length in the a1 direction
        m = the length in the a2 direction
        l = the length between hexagonal coordinates
    output:
        pos_gr
    '''
    Cf = CarbonFiller (n, m, l)
    Ch = Cf.vector()
    T = Cf.TVector(Ch)
    
    p, q = Cf.pq(Ch , T)
    
    Pgrid , Qgrid = grid_pq (p, q)
    
    x, y = Cf.coordinates(Pgrid, Qgrid)
 
    c_hat , arclen = Cf.normVector(Ch)
    s, t = Cf.distance (x, y, c_hat )
    
    pos_gr = include_atoms_gr(x, y, s, t, arclen , l)
    return pos_gr

"""
This is a class to construct carbon nanofillers, e.g. Graphene sheets and/
or carbon nanotubes.
"""
    
class CarbonFiller:

    '''
    This is a functionInitializes the CarbonFiller object with values n, m, and l
    input:
        n = the length in the a1 direction
        m = the length in the a2 direction
        l = the length between hexagonal coordinates
    '''
    def __init__(self, n, m , l):
        self.name = 'Carbon Filler'
        self.n = n
        self.m = m
        self.l = l
        
 
    def vector(self):
        '''
        This is a function that returns the carbonfiller Ch as a vector in the 
        cartesian coordinate plane as a numpy array.
        no input
        output:
            vec: carbonfiller Ch as a vector in xy, cartesian plane
        '''   
        vec = np.array(np.round([sq3 * self.n + self.m / 2*sq3, self.m * -1.5],3))
        return vec

    def TVector(self, Ch):
        '''
        This function accepts a numpy array and returns the normalized perpendicular vector
        Input:
            Ch: (2,) array of coordinates for Carbonfiller
        Output:
            T: normalized perpendicular vector to Ch
        '''
        T, useless = self.normVector(Ch)       #Ch = self.vector()
        T = self.normTvector(T) * self.l
        return T
    

    @staticmethod
    def normVector(vec):
        '''
        This is a static function that accepts the CarbonFiller vector as a numpy array and returns
        the normalized (directional) vector
        Input:
            vec: any vector
        Output:
            normvec: normalized vector
            norm: length of vec
        '''
        norm = np.round(np.sqrt(np.dot(vec,vec)),3)
        normvec = np.round(vec/norm, 3)
        return normvec, norm

    @staticmethod
    def normTvector(c_hat):
        '''
        This is a static funcion that accepts a numpy array of the coordinates in the cartesian plane
        and returns the normal vector to that with the same length
        Input: 
            c_hat: a normalized vector
        Output:
            t_hat: perpendicular vector to c_hat
        '''
        t_hat = np.array([-c_hat[1], c_hat[0]])
        return t_hat
        

    @staticmethod    
    def pq(Ch, T):
        '''
        This is a static method that accepts a vector Ch and its perpendicular vector T, that outputs
        the rectilinear sheet in the p,q coordinate plane that can contain the graphene sheet
        Input:
            Ch: vector of carbonfiller
            T: perpendicular vector to Ch
        Output:
            [p_min, p_max]: min and max values of p coordinates of Ch and T in p,q coordinates
            [q_min, q_max]: min and max values of q coordinates of Ch and T in p,q coordinates
        '''
        v4 = np.add(Ch,T)
        p_max = math.ceil(max(0,Ch[0], T[0], v4[0])*2/sq3)
        p_min = math.floor(min(0,Ch[0], T[0], v4[0])/sq3)
        q_max = math.ceil(max(0,Ch[1], T[1], v4[1])/1.5)
        q_min = math.floor(min(0,Ch[1], T[1], v4[1])/1.5)
        return np.array([ p_min , p_max ]), np.array([ q_min , q_max ])
    

    @staticmethod
    def coordinates(pg, qg):
        '''
        This is a static method that accepts a 2 lists of coordinates in the p,g plane and converts 
        them to points in the hexagonal plane
        Input:
            pg: a 2_D array of all p values
            qg: a 2_D array of all q values
        Output:
            x: 2_D array of x coords in cartesian plane
            y: 2_D array of y coords in cartesian plane 
            
        '''
        y = list(qg)
        x = np.round(np.multiply(pg, sq3/2),3)
        
        for i in range(len(qg)):
            mod = np.mod(qg[i],2)
            y[i] = np.multiply(qg[i],1.5) + np.multiply(np.mod(pg[i]+mod,2), -0.5)

        return x, np.array(y)
    

    @staticmethod
    def distance(x, y, c_hat):
        '''
        This static method takes in 2 2-D arrays x,y that contain the coordinates of the atoms and in
        the x,y plane. c_hat that contains the coordinates of normal vector. it returns and array of
        the distance in the tube direction, t and along the mouth, s via dot product
        Input:
            x: 2_D array of cartesian x coords of nodes
            y: 2_D array of cartesian y coords of nodes
            c_hat: (2,) array of normalized Ch vector
        Output:
            t: tube distance between nodes
            s: mouth distance between nodes
        '''
        nx = c_hat[0]
        ny = c_hat[1]
        t = np.round(np.multiply(-ny, x) + np.multiply(nx, y),3)
        s = np.round(np.multiply(nx, x) + np.multiply(ny, y), 3)
        return s, t
    
    
if __name__ == '__main__':  
    # x1, y1 = CarbonFiller.coordinates([[0, 1, 2], [0, 1, 2]], [[0, 0, 0], [1,
    # 1, 1, ]])
    x2, y2 = CarbonFiller.coordinates([[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 0, 0, 1, 1], [1,
    1, 1, 2,2]])
    #plt.plot(x2, y2,  marker = 'o', markersize = 12, markerfacecolor = 'red')
    
    # print(CarbonFiller(2, 1, 1).TVector([4.33, -1.5]))
    # # print(Graphene(5, 6, 1))
    
    Ch1 = [4.33, -1.5]       #pass
    Ch2 = [10.392, -6]       #fail
    b = CarbonFiller(1, 1, 4)
    a = CarbonFiller(4, 4, 1)
    # print(CarbonFiller(2, 1, 1).TVector([4.33, -1.5]))
    # print(a.TVector([10.392, -6]))
    # print(b.TVector([10.392, -6]))
    # print(graph.TVector(Ch1))
    
        
        
        
        
        
        
        


