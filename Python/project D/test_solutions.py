# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:29:23 2022

@author: willi
"""

import numpy as np
import math
import matplotlib as plt
from plot_nano import *
from misc import include_atoms_gr,  grid_pq
from solution import Graphene



if __name__ == '__main__':  
    # #test 1
    pos = Graphene(-14,4,18)       
    '''
    l allowed is slightly larger than what is given, ie l allowed is 2.59 but l is 2.5
    '''
    lowth = 0.95
    upth = 1.05
    xx ,yy = get_connectivity_ind (pos, lowth , upth )
    plot_mesh (xx ,yy ,pos)

    # #test 2
    # pos = Graphene(5,0,5)

    # lowth = 0.95
    # upth = 1.05
    # xx ,yy = get_connectivity_ind (pos, lowth , upth )
    # plot_mesh (xx ,yy ,pos)

    #test 3
    # pos = Graphene(2,2,1)

    # lowth = 0.95
    # upth = 1.05
    # xx ,yy = get_connectivity_ind (pos, lowth , upth )
    # plot_mesh (xx ,yy ,pos)
    