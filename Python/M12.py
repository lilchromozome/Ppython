# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:01:27 2022

@author: willi
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# nums = np.linspace(-2,2,1000)
# approx = 1 + (nums**2)/2
# fr = np.cosh(nums)

# plt.figure()
# plt.plot(nums, approx)
# plt.plot(nums, fr)
# plt.title('cosh(x) vs parabolic approximation')
# plt.text(-1.8, 3.5, '(-1.8, 3.5) cosh(x)')
# plt.text(-1.8, 1.2, '(-1.8, 1.2) parabolic estimations')
# plt.legend(['approx', 'cosh(x)'], loc = 'upper right')


# countries = ['Brazil', 'Madagascar', 'S. Korea', 'United States', 'Ethiopia', 'Pakistan', 'China', 'Belize']
# birth_rate = [16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0]
# life_expectancy = [73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7]
# capita_gdp = np.array([4800, 240, 16700, 37700, 230, 670, 2640, 3490])
# capita = capita_gdp/10


# plt.figure()
# plt.scatter(birth_rate, life_expectancy, s= capita)
# plt.xlabel('Birth rate per 1000')
# plt.ylabel('Life expectancy at birth (years)')


data = np.loadtxt('trees.csv', delimiter=",", skiprows=1)

print(data)