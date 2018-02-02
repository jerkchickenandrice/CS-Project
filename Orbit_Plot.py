from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import animation as animation
import numpy as np
import math
x_vel = 0
y_vel = 0
style.use('ggplot')
#plt.plot(0, 0, marker='o', markersize=10, color="orange") # The Sun 
x = []
y = []
count = 0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

        
def animate(i):
    global x_vel
    global y_vel
    movement = (x_vel)**2 + (y_vel)**2
    sqrt = movement**(.5)
    print(sqrt)
    y.append(sqrt -1)
    x.append(sqrt -3)
    ax1.clear()
    ax1.scatter(x,y)
    x_vel = x_vel + 1
    y_vel = y_vel + 1

    
ani = animation.FuncAnimation(fig, animate, interval = 10) #A class functions which loops the drawing of the chart
ax1.set_xlim([-20,20])
ax1.set_ylim([-20,20])
plt.show()

