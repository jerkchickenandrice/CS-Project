from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import animation as animation
import numpy as np
import math
import tkinter
from tkinter import *

style.use('dark_background')
fig = plt.figure()

x_pos_1 = [10]
y_pos_1 = [0]

x_pos_2 = [6]
y_pos_2 = [0]

x_pos_3 = [-4]
y_pos_3 = [0]

vel_x_1 = -0.00
vel_y_1 = 0.1

vel_x_2 = 0.00
vel_y_2 = 0.1

vel_x_3 = 0.00
vel_y_3 = 0.2

mass_1 = 150
mass_2 = 150
mass_3 = 150 

distance = 0
count = 0
G = 0.00000005
m_sun = 2250000
timestep = 1
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)

def animate(i):

    def planet_1():
        global distance
        global vel_y_1
        global vel_x_1
        global G
        global count
        
        distance = (x_pos_1[count])**2 +(y_pos_1[count])**2
        sqrt = distance**(0.5)
        F = (G * mass_1 * m_sun) / sqrt**2
        dirX = -x_pos_1[count] # direction vector from 0,0 to the planet x,y
        dirY = -y_pos_1[count]
    
        Vec_magnitude  = (dirX**2 + dirY**2)**0.5
    
        Fx = dirX * (F / Vec_magnitude) #Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_1[count] + vel_x_1
        y_tem_pos = y_pos_1[count] + vel_y_1
        
        x_pos_1.append(x_tem_pos)
        y_pos_1.append(y_tem_pos)
    
        Acc_x = Fx / mass_1
        Acc_y = Fy / mass_1
    
        vel_x_1 += Acc_x
        vel_y_1 += Acc_y
        
        
        ax1.clear()
        ax1.scatter(x_pos_1,y_pos_1)
        ax2.scatter(0, 0)
        ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
        #print(x_pos,y_pos)

    def planet_2():
        global distance
        global vel_y_2
        global vel_x_2
        global G
        global count
        
        distance = (x_pos_2[count])**2 +(y_pos_2[count])**2
        sqrt = distance**(0.5)
        F = (G * mass_2 * m_sun) / sqrt**2
        dirX = -x_pos_2[count] # Direction vector from 0,0 to the planet x,y
        dirY = -y_pos_2[count]
    
        Vec_magnitude  = (dirX**2 + dirY**2)**0.5
    
        Fx = dirX * (F / Vec_magnitude) # Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_2[count] + vel_x_2
        y_tem_pos = y_pos_2[count] + vel_y_2
        
        x_pos_2.append(x_tem_pos)
        y_pos_2.append(y_tem_pos)
    
        Acc_x = Fx / mass_2
        Acc_y = Fy / mass_2
    
        vel_x_2 += Acc_x
        vel_y_2 += Acc_y
        
        
        ax1.scatter(x_pos_2,y_pos_2)
        ax2.scatter(0, 0)
        ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
        #print(x_pos,y_pos)

    def planet_3():
        
        global distance
        global vel_y_3
        global vel_x_3
        global G
        global count
        
        distance = (x_pos_3[count])**2 +(y_pos_3[count])**2
        sqrt = distance**(0.5)
        F = (G * mass_1 * m_sun) / sqrt**2
        dirX = -x_pos_3[count] # direction vector from 0,0 to the planet x,y
        dirY = -y_pos_3[count]
    
        Vec_magnitude  = (dirX**2 + dirY**2)**0.5
    
        Fx = dirX * (F / Vec_magnitude) #Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_3[count] + vel_x_3
        y_tem_pos = y_pos_3[count] + vel_y_3
        
        x_pos_3.append(x_tem_pos)
        y_pos_3.append(y_tem_pos)
    
        Acc_x = Fx / mass_3
        Acc_y = Fy / mass_3
    
        vel_x_3 += Acc_x
        vel_y_3 += Acc_y
        
        count = count + 1

        ax1.scatter(x_pos_3,y_pos_3)
        ax2.scatter(0, 0)
        ax1.get_xaxis().get_major_formatter().set_scientific(False)
        #ax1.set_xlim([-25,25])
        #ax1.set_ylim([-25,25])
    planet_1()
    planet_2()
    planet_3()                         

ani = animation.FuncAnimation(fig, animate, interval = 100) #A class functions which loops the drawing of the chart
plt.show()
