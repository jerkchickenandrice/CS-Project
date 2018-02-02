from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import animation as animation
import numpy as np
import math

style.use('dark_background')
x_pos = [7]
y_pos = [0]
distance = 0
count = 0
G = 0.00000005
m_earth = 150
m_sun = 2250000

vel_y = 0.1
vel_x = 0

timestep = 1

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)

def bin():
    global distance
    global vel_y
    global vel_x
    global G
    global count 
      
    distance = (x_pos[count])**2 +(y_pos[count])**2
    sqrt = distance**(0.5)
    #print(sqrt)    
    F = (G * m_earth * m_sun) / sqrt**2
    
    theta = math.atan2(y_pos[count],x_pos[count]) # Angle between the positive x axis and the point 

    Fx = math.cos(theta) * -F
    Fy = math.sin(theta) * -F
        
    #print(Fx)

    
    x_tem_pos = x_pos[count] + vel_x
    y_tem_pos = y_pos[count] + vel_y
        
    x_pos.append(x_tem_pos)
    y_pos.append(y_tem_pos)

    vel_x += Fx /(m_earth)
    #print(vel_x)
    vel_y += Fy /(m_earth)
    
    count = count + 1
    
    
    
    ax1.clear()
    ax1.scatter(x_pos,y_pos)
    ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
    #print(x_pos,y_pos)
    pass

def animate(i):
    global distance
    global vel_y
    global vel_x
    global G
    global count 
      
    distance = (x_pos[count])**2 +(y_pos[count])**2
    sqrt = distance**(0.5)
    F = (G * m_earth * m_sun) / sqrt**2
    dirX = -x_pos[count] # direction vector from 0,0 to the planet x,y
    dirY = -y_pos[count]
    
    Vec_magnitude  = (dirX**2 + dirY**2)**0.5
    
    Fx = dirX * (F / Vec_magnitude) #Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
    Fy = dirY * (F / Vec_magnitude)
     
    x_tem_pos = x_pos[count] + vel_x
    y_tem_pos = y_pos[count] + vel_y
        
    x_pos.append(x_tem_pos)
    y_pos.append(y_tem_pos)
    
    Acc_x = Fx / m_earth
    Acc_y = Fy / m_earth
    
    vel_x += Acc_x
    vel_y += Acc_y

    count = count + 1
    
    ax1.clear()
    ax1.scatter(x_pos,y_pos)
    ax1.set_title('Orbital Simulation') 
    ax1.set_ylabel('Vertical Distance from Sun')
    ax1.set_xlabel('Horizontal Distance from Sun')
    ax2.scatter(0, 0)
    ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
    #print(x_pos,y_pos)

    
ani = animation.FuncAnimation(fig, animate, interval = 1) #A class functions which loops the drawing of the chart
ax1.set_xlim([-200,200])
ax1.set_ylim([-200,200])

plt.show()    
   
