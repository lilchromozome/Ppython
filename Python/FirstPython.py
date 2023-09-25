# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 14:45:33 2022

@author: willi
"""
import matplotlib.pyplot as plt
import numpy as np

game = True
White = 0       #1     112  32.8%
Black = 0       #2     72   21.1%
Asian = 0       #3     85   24.9%
Hispanic = 0    #4     33   9.7%
Indian = 0      #5     39   11.0%
temp = [White, Black, Asian, Hispanic, Indian]
Fr = [White, Black, Asian, Hispanic, Indian]



while game:
        guess = int(input("Enter Race"))
        if guess == 10:
            game = False
            print("White = " + str(Fr[0]) + "\nBlack = " + str(Fr[1])
                  + "\nAsian = " + str(Fr[2]) + "\nHispanic = " + str(Fr[3])
                  + "\nIndian = " + str(Fr[4]))
            
        if guess == 0:
            Fr = temp
        if guess == 1:
            temp = [White, Black, Asian, Hispanic, Indian]
            print("White")
            White+=1
            Fr = [White, Black, Asian, Hispanic, Indian]
        if guess == 2:
            temp = [White, Black, Asian, Hispanic, Indian]
            print("Black")
            Black+=1
            Fr = [White, Black, Asian, Hispanic, Indian]
        if guess == 3:
            temp = [White, Black, Asian, Hispanic, Indian]
            print("Asian")
            Asian+=1
            Fr = [White, Black, Asian, Hispanic, Indian]
        if guess == 4:
            temp = [White, Black, Asian, Hispanic, Indian]
            print("Hispanic")
            Hispanic+=1
            Fr = [White, Black, Asian, Hispanic, Indian]
        if guess == 5:
            temp = [White, Black, Asian, Hispanic, Indian]
            print("Indian")
            Indian+=1
            Fr = [White, Black, Asian, Hispanic, Indian]
total = White + Black + Asian + Hispanic + Indian


y = np.array([White, Black, Asian, Hispanic, Indian])
mylabels = ["White " + str(round(White/total,3)*100) +"%", 
            "Black " + str(round(Black/total,3)*100) +"%",
            "Asian " + str(round(Asian/total,3)*100) +"%", 
            "Hispanic " + str(round(Hispanic/total,3)*100) +"%",
            "Indian " + str(round(Indian/total,2)*100) +"%"]
plt.pie(y, labels = mylabels)
plt.show() 
        
            