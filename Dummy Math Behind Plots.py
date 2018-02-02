from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import animation as animation
import numpy as np
import math

style.use('dark_background')
x_pos = [5]
y_pos = [0]

x_pos_2 = [10]
y_pos_2 = [0]

x_pos_3 = [-20]
y_pos_3 = [0]

vel_x = -0.03
vel_y = 0.1

vel_x_2 = 0.03
vel_y_2 = 0.07

vel_x_3 = 0.05
vel_y_3 = 0.05

distance = 0
count = 0
G = 0.00000005
m_earth = 100
m_sun = 15000

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

    def planet_1():
        global distance
        global vel_y
        global vel_x
        global G
        global count 
        distance = (x_pos[count])**2 +(y_pos[count])**2
        sqrt = distance**(0.5)
        A = (G * m_earth * m_sun) / sqrt**2
        dirX = -x_pos[count]
        dirY = -y_pos[count]
        mag = (dirX**2 + dirY**2)**0.5
        Ax = dirX * (A / mag)
        Ay = dirY * (A / mag)
        
        #print(Fx)
        
        x_tem_pos = x_pos[count] + vel_x
        y_tem_pos = y_pos[count] + vel_y
            
        x_pos.append(x_tem_pos)
        y_pos.append(y_tem_pos)

        vel_x += Ax
        vel_y += Ay
        
        
        ax1.clear()
        ax1.scatter(x_pos,y_pos)
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
        A = (G * m_earth * m_sun) / sqrt**2
        dirX = -x_pos_2[count]
        dirY = -y_pos_2[count]
        mag = (dirX**2 + dirY**2)**0.5
        Ax = dirX * (A / mag)
        Ay = dirY * (A / mag)
        
        #print(Fx)
        
        x_tem_pos = x_pos_2[count] + vel_x_2
        y_tem_pos = y_pos_2[count] + vel_y_2
            
        x_pos_2.append(x_tem_pos)
        y_pos_2.append(y_tem_pos)

        vel_x_2 += Ax
        vel_y_2 += Ay
        print("vel", vel_x, vel_y)
        
        
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
        A = (G * m_earth * m_sun) / sqrt**2
        dirX = -x_pos_3[count]
        dirY = -y_pos_3[count]
        mag = (dirX**2 + dirY**2)**0.5
        Ax = dirX * (A / mag)
        Ay = dirY * (A / mag)
        
        #print(Fx)
        
        x_tem_pos = x_pos_3[count] + vel_x_3
        y_tem_pos = y_pos_3[count] + vel_y_3
            
        x_pos_3.append(x_tem_pos)
        y_pos_3.append(y_tem_pos)

        vel_x_3 += Ax
        vel_y_3 += Ay
        print("vel", vel_x, vel_y)
        count = count + 1

        ax1.scatter(x_pos_3,y_pos_3)
        ax2.scatter(0, 0)
        ax1.get_xaxis().get_major_formatter().set_scientific(False)
    planet_1()
    planet_2()
    planet_3()
        
ani = animation.FuncAnimation(fig, animate, interval = 10) #A class functions which loops the drawing of the chart
ax1.set_xlim([-200,200])
ax1.set_ylim([-200,200])

plt.show()    
   
