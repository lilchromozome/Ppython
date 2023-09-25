#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:17:02 2022

@author: 
"""

import numpy as np
import matplotlib.pyplot as plt



def find_connectivity(points , low_th = 0.95, up_th = 1.05):
    '''
    This method finds the euclidean distance between all points provided in the 2D array points that are
    within the upper bound up_th and lower bound low_th, returning an array of the acceptable distances
    in a 2D array
    input:
        points: a two-dimensional (2D) numpy array that contains x and y coordinates of
            points in 2D space. Accordingly, this numpy array will have a dimension of number
            of points × 2.
        low th: a scalar float quantity defines the lower accepted threshold values for the
            Euclidean distance squared value. Default 0.95.
        up th: a scalar float quantity defines the upper accepted threshold values for the
            Euclidean distance squared value. Default 1.05.
    output:
        DistMat: a square 2D array with dimensions of len(points) that contain the distances
        between each point
    '''
    a = len(points)
    DistMat = []
    allx = points[:,0]
    ally = points[:,1]
    for i in range(a):
        f = (list(np.power((allx - points[i,0]),2) + np.power(ally - points[i,1],2)))
        for j in range(a):
            if f[j] > 1:
                f[j] = 0
        DistMat.append(f)
    return np.array(DistMat)


def get_connectivity_ind(points , low_th = 0.95, up_th = 1.05):
    '''
    This method finds the x and y indices of all points provided in the 2D array points that have 
    a distance within the upper bound up_th and lower bound low_th
    input:
        points: a two-dimensional (2D) numpy array that contains x and y coordinates of
            points in 2D space. Accordingly, this numpy array will have a dimension of number
            of points × 2.
        low_th: a scalar float quantity defines the lower accepted threshold values for the
            Euclidean distance squared value. Default 0.95.
        up_th: a scalar float quantity defines the upper accepted threshold values for the
            Euclidean distance squared value. Default 1.05.
    output:
        index_points_limits: This function should return two numpy arrays, which are indexes of 
            points where the distance squared is within the defined limit. the first numpy array 
            contains the indexes for the first points and the second array contains the indexes 
            for the second set of points.
        
    '''
    index_points_limits = []
    index_points_x = []
    index_points_y = []
    vals = find_connectivity(points , low_th, up_th)
    for i in range(len(vals)):
        for j in range(i, len(vals)):
            if vals[i,j] != 0:
                index_points_x.append(i)
                index_points_y.append(j)
    index_points_limits = np.vstack((np.array(index_points_x), np.array(index_points_y)))
    return index_points_limits


def plot_mesh(xx, yy, a):        ##ALL3 ARE ARRAYS
    '''
    This is a method that takes in 3 arrays, the x values, y values, and array and outputs the
    scatter chart of those points using plot_carbon_carbon
    input:
        xx: array of all x values
        yy: array of all y values
        a: array of all points
    output:
        matplot lib scatter plot of the points
    '''

    for i in range(len(xx)):
        p1 = int(xx[i])
        p2 = int(yy[i])
        plot_carbon_carbon(a[p1],a[p2])
    return       
            

def plot_carbon_carbon(p1, p2):
    '''
    This is a function that returns a graph that connects 2 points p1 and p2
    input:
        p1, p2: a (2,) array of the coordinates of the poits
    output:
        a matplotlib plot that joins the 2 points

    '''
    plt.plot([p1[0],p2[0]], [p1[1],p2[1]], linestyle = '-', color = 'blue', marker = 'o', markersize = 4, markerfacecolor = 'red')
    return

if __name__ == '__main__':  
    # pp = np.array([[0.98741274 , 0.45638062] ,[0.01421964 , 0.90581148] , [0.30552894 , 0.03409079]])
    # xx ,yy = get_connectivity_ind (pp ,0.5 ,1)
    # print(xx ,yy)
    # [0 1] [2 2]
    # 0 -> 2, 1 -> 2 are good
    
    # p1 = np.array ([0.98741274 , 0.45638062])
    # p2 = np.array ([0.30552894 , 0.03409079])
    # plot_carbon_carbon (p1 ,p2)

    # a = np.array ( [[0. , 0. ],
    #                 [2.598 , 1.5 ],
    #                 [1.732 , 1. ],
    #                 [0.866 , 1.5 ],
    #                 [0. , 1. ],
    #                 [5.196 , 3. ],
    #                 [4.33 , 2.5 ],
    #                 [3.464 , 3. ],
    #                 [2.598 , 2.5 ]])
    
    
    a = np.array(
      [[0.,    0.   ],
      [1.732, 0.   ],
      [3.464, 0.   ],
      [5.196, 0.   ],
      [6.928, 0.   ],
      [0.,    1.   ],
      [0.866, 1.5  ],
      [1.732, 1.   ],
      [2.598, 1.5  ],
      [3.464, 1.   ],
      [4.33,  1.5  ],
      [5.196, 1.   ],
      [6.062, 1.5  ],
      [6.928, 1.   ]])
    
    lowth = 0.95
    upth = 1.05
    xx ,yy = get_connectivity_ind (a, lowth , upth )
    plot_mesh (xx ,yy ,a)
    # plot_carbon_carbon(xx,yy)


    pass
  