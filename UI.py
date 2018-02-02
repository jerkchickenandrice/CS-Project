"""from matplotlib import pyplot as plt
from matplotlib import animation as animation
from matplotlib import style
style.use('dark_background')


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


x_pos = [2]
y_pos = [4]

count = 0

def animate(i):
    global count 
    
    x_pos.append(x_pos[count] + 1)
    y_pos.append(y_pos[count] + 1)

    count += 1
    
    ax1.clear()
    ax1.set_title('Orbital Simulation') 
    ax1.set_ylabel('Vertical Distance from Sun')
    ax1.set_xlabel('Horizontal Distance from Sun')
    ax1.scatter(x_pos,y_pos)
    
ani = animation.FuncAnimation(fig, animate, interval = 500) #A class functions which loops the drawing of the chart
plt.show()


"""
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import animation as animation
import numpy as np
import math

style.use('dark_background')

x_pos = [5]
y_pos = [0]
vel_y = 1
vel_x = 0
G = 0.000009
m_earth = 200
m_sun = 999000
count = 0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    global count
    global vel_x
    global vel_y
    global G
    
    distance = (x_pos[count])**2 + (y_pos[count])**2
    
    sqrt = distance**(0.5)
    
    F = (G * m_earth * m_sun)/sqrt**2
    
    theta = math.atan2(y_pos[count],x_pos[count])
    
    Fx = math.cos(theta) * -F
    Fy = math.sin(theta) * -F
    
    x_tem_pos = x_pos[count] + vel_x
    y_tem_pos = y_pos[count] + vel_y
    
    x_pos.append(x_tem_pos)
    y_pos.append(y_tem_pos)
    
    vel_x += Fx /(m_earth)
    vel_y += Fy /(m_earth)
    
    count = count + 1
    
    ax1.clear()
    ax1.set_title('Orbital Simulation') 
    ax1.set_ylabel('Vertical Distance from Sun')
    ax1.set_xlabel('Horizontal Distance from Sun')
    ax1.scatter(x_pos,y_pos)
    ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only


ani = animation.FuncAnimation(fig, animate, interval = 1000) #A class functions which loops the drawing of the chart
plt.show()
