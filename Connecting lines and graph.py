from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import animation as animation
import numpy as np
import math
import tkinter
from tkinter import *
from decimal import *
number_planet = 1

class Simulator(Frame):

    def __init__(self,interface):
        
        'Initialize the Frame'
        
        Frame.__init__(self, interface)
        interface.minsize(width = 1000, height = 500)
        interface.maxsize(width = 1000, height = 500)
        interface.resizable(width=False, height=False)
        self.grid()
        self.create_widgets()
        
        
    def create_widgets(self):

        Start_Sim_Button = Button(self, text="START", fg="green", command = self.start_orbit)
        Start_Sim_Button.grid(row=1,column=1,columnspan = 1)

        instruction = Label(self, text = "Number of Planets")
        instruction.grid(row=2,column=1,columnspan=1)
        
        self.num_planet = IntVar()
        Radiobutton(self, text="1", variable=self.num_planet, value=1, command = self.option_planet).grid(row=2, column = 2)
        Radiobutton(self, text="2", variable=self.num_planet, value=2, command = self.option_planet).grid(row=2, column = 3)
        Radiobutton(self, text="3", variable=self.num_planet, value=3, command = self.option_planet).grid(row=2, column = 4)
        
        orbit_choice = IntVar()
        Radiobutton(self,text='Orbital Paths?', indicatoron = 0, width = 15,variable=orbit_choice, command=self.orb_path , value=1).grid(row = 1, column =2)

        save_variables_button = Button(self, text = 'Save Variables', fg = 'blue', command = self.save_variables)
        save_variables_button.grid(row=1,column=3)
        
        #-------------Velocity In X-----------------
            
        vel_label=Label(self, text = 'Velocity X Green Planet')
        vel_label.grid(row=4,column=1)
        velocityX_1 = Scale(self, from_=-10, to=10, orient = HORIZONTAL , command = self.vel_x_1, resolution = 0.1)
        velocityX_1.grid(row=4, column=2)

        if number_planet == 2 or number_planet == 3:
            
            vel_label=Label(self, text = ' Velocity X Purple Planet')
            vel_label.grid(row=4,column=3)
            velocityX_2 = Scale(self, from_=-10, to=10, orient = HORIZONTAL, command = self.vel_x_2, resolution = 0.1)
            velocityX_2.grid(row=4, column=4)
            
        if number_planet == 3 :
            
            vel_label=Label(self, text = ' Velocity X Red Planet')
            vel_label.grid(row=4,column=5)
            velocityX_3 = Scale(self, from_=-10, to=10, orient = HORIZONTAL, command = self.vel_x_3, resolution = 0.1)
            velocityX_3.grid(row=4, column=6)
            
        #-------------Velocity In Y-----------------
        vel_label=Label(self, text = 'Velocity Y Green Planet')
        vel_label.grid(row=5,column=1)
        velocityY_1 = Scale(self, from_=-10, to=10, orient = HORIZONTAL,command = self.vel_y_1, resolution = 0.1)
        velocityY_1.grid(row=5, column=2)
        
        if number_planet == 2 or number_planet == 3:
            
            vel_label=Label(self, text = ' Velocity Y Purple Planet')
            vel_label.grid(row=5,column=3)
            velocityY_2 = Scale(self, from_=-10, to=10, orient = HORIZONTAL, command = self.vel_y_2, resolution = 0.1)
            velocityY_2.grid(row=5, column=4)
            
        if number_planet == 3 :
            
            vel_label=Label(self, text = ' Velocity Y Red Planet')
            vel_label.grid(row=5,column=5)
            velocityY_3 = Scale(self, from_=-10, to=10, orient = HORIZONTAL, command = self.vel_y_3, resolution = 0.1)
            velocityY_3.grid(row=5, column=6)
        #-------------Position------------------
        pos_label=Label(self, text = 'Position Green Planet')
        pos_label.grid(row=6, column=1)
        position_1 = Scale(self, from_=-5, to=5, orient=HORIZONTAL, command = self.position_1, resolution = 0.1)
        position_1.grid(row=6,column=2)

        if number_planet == 2 or number_planet == 3:
        
            pos_label=Label(self, text = ' Position Purple Planet')
            pos_label.grid(row=6, column=3)
            position_2 = Scale(self, from_=-5, to=5, orient=HORIZONTAL, command = self.position_2, resolution = 0.1)
            position_2.grid(row=6,column=4)
            
        if number_planet == 3 :
            
            pos_label=Label(self, text = ' Position Red Planet')
            pos_label.grid(row=6, column=5)
            position_3 = Scale(self, from_=-5, to=5, orient=HORIZONTAL, command = self.position_3, resolution = 0.1)
            position_3.grid(row=6,column=6)
        #-------------Mass--------------------
        mass_label=Label(self, text = 'Mass Green Planet')
        mass_label.grid(row=7,column=1)
        mass_1 = Scale(self, from_=0, to=1000, orient=HORIZONTAL, command = self.mass_1)
        mass_1.grid(row=7, column=2)

        if number_planet == 2 or number_planet == 3:
        
            mass_label=Label(self, text = ' Mass of Purple Planet')
            mass_label.grid(row=7,column=3)
            mass_2 = Scale(self, from_=0, to=1000, orient=HORIZONTAL,command = self.mass_2)
            mass_2.grid(row=7, column=4)
        
        if number_planet == 3 :
            
            mass_label=Label(self, text = ' Mass of Red Planet')
            mass_label.grid(row=7,column=5)
            mass_3 = Scale(self, from_=0, to=1000, orient=HORIZONTAL, command = self.mass_3)
            mass_3.grid(row=7, column=6)

       # self.planet_one = BooleanVar()
        #Checkbutton(self,text="1", variable = self.planet_one, command = self.num_planets).grid(row=1,column=8,columnspan=1)
        
        #self.planet_two = BooleanVar()
        #Checkbutton(self,text="2", variable = self.planet_two, command = self.num_planets).grid(row=1,column=9,columnspan=1)
        
        #self.planet_three = BooleanVar()
        #Checkbutton(self,text="3", variable = self.planet_three, command = self.num_planets).grid(row=1,column=10,columnspan=1)

    def save_variables(self):
        file = open("Simulation_Variables.txt","w+")
        file.write("Velocity X Green Planet = " + str(vel_x_1*100) + "   Velocity X Purple Planet = " + str(vel_x_2*100) + "   Velocity X Red Planet = " + str(vel_x_3*100)+ "\n")
        file.write("Velocity Y Green Planet = " + str(vel_y_1*100) + "   Velocity Y Purple Planet = " + str(vel_y_2*100) + "   Velocity Y Red Planet = " + str(vel_y_3*100)+ "\n")
        file.write("Position Green Planet   = " + str(x_pos_1[0])  + "   Position Purple Planet   = " + str(x_pos_2[0]) +  "   Position Red Planet   = " + str(x_pos_3[0])+ "\n")
        file.write("Mass of Green Planet    = " + str(mass_1)      + "   Mass of Purple Planet    = " + str(mass_2) +      "   Mass of Red Planet    = " + str(mass_3)+ "\n")
        
    def option_planet(self):

        
            global number_planet
            
            if self.num_planet.get() == 1 :
                number_planet = 1
            if self.num_planet.get() == 2 :
                number_planet = 2
            if self.num_planet.get() == 3 :
                number_planet = 3
            self.create_widgets()
            
    def orb_path(self):
        global orbit_choice
        orbit_choice = True

                
    def vel_x_1(self,tempval):
        global vel_x_1
        vel_x_1 = Decimal(tempval)/Decimal(100)
        
    def vel_x_2(self,tempval):
        global vel_x_2
        vel_x_2 = Decimal(tempval)/Decimal(100)
        
    def vel_x_3(self,tempval):
        global vel_x_3
        vel_x_3 = Decimal(tempval)/Decimal(100)
    
    def vel_y_1(self,tempval):
        global vel_y_1
        vel_y_1 = Decimal(tempval)/Decimal(100)
        
    def vel_y_2(self,tempval):
        global vel_y_2
        vel_y_2 = Decimal(tempval)/Decimal(100)
    
    def vel_y_3(self,tempval):
        global vel_y_3
        vel_y_3 = Decimal(tempval)/Decimal(100)
        
    def position_1(self,tempval):
        global position_1
        position_1 = Decimal(tempval)
        x_pos_1[0] = (position_1)
        
    def position_2(self,tempval):
        global position_2
        position_2 = Decimal(tempval)
        x_pos_2[0]=(position_2)

    def position_3(self,tempval):
        global position_3
        position_3 = Decimal(tempval)
        x_pos_3[0]=(position_3)
    
    def mass_1(self,tempval):
        global mass_1
        mass_1 = int(tempval)
        
    def mass_2(self,tempval):
        global mass_2
        mass_2 = int(tempval)
    
    def mass_3(self,tempval):
        global mass_3
        mass_3 = int(tempval)
        

    
    def num_planets(self):
        
        if self.planet_one.get():
            writing=Label(self, text = '1 Planet')
            writing.grid(row=10,column=10)
        elif self.planet_two.get():
            writing=Label(self, text = '2 Planets')
            writing.grid(row=10,column=10)
        elif self.planet_three.get():
            writing=Label(self, text = '2 Planets')
            writing.grid(row=10,column=10)

    def start_orbit(self):
            ani = animation.FuncAnimation(fig, animate, interval = 10) #A class functions which loops the drawing of the chart
            plt.show()
    


def animate(i):
    global number_planet
    global count
    
    def planet_1():
        global distance
        global vel_y_1
        global vel_x_1
        global G
        
        distance = (x_pos_1[count])**2 +(y_pos_1[count])**2
        sqrt = Decimal(distance)**Decimal(0.5)
        F = Decimal(G * mass_1 * m_sun) / Decimal(sqrt)**Decimal(2)
        dirX = Decimal(-x_pos_1[count]) # direction vector from 0,0 to the planet x,y
        dirY = Decimal(-y_pos_1[count])
    
        Vec_magnitude  = (Decimal(dirX)**Decimal(2) + Decimal(dirY)**Decimal(2))**Decimal(0.5)
    
        Fx = dirX * (F / Vec_magnitude) #Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_1[count] + Decimal(vel_x_1)
        y_tem_pos = y_pos_1[count] + Decimal(vel_y_1)
        
        x_pos_1.append(x_tem_pos)
        y_pos_1.append(y_tem_pos)
    
        Acc_x = Fx / mass_1
        Acc_y = Fy / mass_1
    
        vel_x_1 = Decimal(Acc_x) + Decimal(vel_x_1)
        vel_y_1 = Decimal(Acc_y) + Decimal(vel_y_1)
        
        
        ax1.clear()
        
        if orbit_choice == True :  
            ax1.plot(x_pos_1, y_pos_1,'-o', markersize=1.0, color = 'C0')
        else:    
            ax1.scatter(x_pos_1,y_pos_1, s = 0.5, color = 'C0')
        
        
        ax2.scatter(0, 0, color ='C1')
        ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
        #print(x_pos,y_pos)

    def planet_2():
        global distance
        global vel_y_2
        global vel_x_2
        global G
        
        distance = (x_pos_2[count])**2 +(y_pos_2[count])**2
        sqrt = Decimal(distance)**Decimal(0.5)
        F = Decimal(G * mass_2 * m_sun) / Decimal(sqrt)**Decimal(2)
        dirX = Decimal(-x_pos_2[count]) # direction vector from 0,0 to the planet x,y
        dirY = Decimal(-y_pos_2[count])
    
        Vec_magnitude  = (Decimal(dirX)**Decimal(2) + Decimal(dirY)**Decimal(2))**Decimal(0.5)
    
        Fx = dirX * (F / Vec_magnitude) #Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_2[count] + Decimal(vel_x_2)
        y_tem_pos = y_pos_2[count] + Decimal(vel_y_2)
        
        x_pos_2.append(x_tem_pos)
        y_pos_2.append(y_tem_pos)
    
        Acc_x = Fx / mass_2
        Acc_y = Fy / mass_2
    
        vel_x_2 = Decimal(Acc_x) + Decimal(vel_x_2)
        vel_y_2 = Decimal(Acc_y) + Decimal(vel_y_2)
        

        if orbit_choice == True :  
            ax1.plot(x_pos_2, y_pos_2,'-o', markersize=1.0, color = 'C2')
        else:    
            ax1.scatter(x_pos_2,y_pos_2, s = 0.5, color = 'C2')

        ax2.scatter(0, 0, color = 'C1')
        ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
        #print(x_pos,y_pos)

    def planet_3():
        
        global distance
        global vel_y_3
        global vel_x_3
        global G
        
        distance = (x_pos_3[count])**2 +(y_pos_3[count])**2
        sqrt = Decimal(distance)**Decimal(0.5)
        F = Decimal(G * mass_3 * m_sun) / Decimal(sqrt)**Decimal(2)
        dirX = Decimal(-x_pos_3[count]) # direction vector from 0,0 to the planet x,y
        dirY = Decimal(-y_pos_3[count])
    
        Vec_magnitude  = (Decimal(dirX)**Decimal(2) + Decimal(dirY)**Decimal(2))**Decimal(0.5)
    
        Fx = dirX * (F / Vec_magnitude) #Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_3[count] + Decimal(vel_x_3)
        y_tem_pos = y_pos_3[count] + Decimal(vel_y_3)
        
        x_pos_3.append(x_tem_pos)
        y_pos_3.append(y_tem_pos)
    
        Acc_x = Fx / mass_3
        Acc_y = Fy / mass_3
    
        vel_x_3 = Decimal(Acc_x) + Decimal(vel_x_3)
        vel_y_3 = Decimal(Acc_y) + Decimal(vel_y_3)

        if orbit_choice == True :  
            ax1.plot(x_pos_3, y_pos_3,'-o', markersize=1.0, color = 'C3')
        else:    
            ax1.scatter(x_pos_3,y_pos_3, s=0.5, color = 'C3')
        
        ax2.scatter(0, 0, color ='C1')
        ax1.get_xaxis().get_major_formatter().set_scientific(False)
        
        
    planet_1()
    if number_planet == 2 or number_planet ==3:
        planet_2()
    if number_planet == 3:
        planet_3()                         
    count = count + 1
    ax1.set_xlim([-5.5,5.5])
    ax1.set_ylim([-5.5,5.5])

    
interface = tkinter.Tk()
GUI = Simulator(interface)
Frame2 = Simulator
   
#Variables and Lists

style.use('dark_background')
fig = plt.figure()
x_pos_1 = [0]
y_pos_1 = [0]

x_pos_2 = [0]
y_pos_2 = [0]

x_pos_3 = [0]
y_pos_3 = [0]

vel_x_1 = 0.00
vel_y_1 = 0.0

vel_x_2 = 0.00
vel_y_2 = 0.00

vel_x_3 = 0.00
vel_y_3 = 0.00

mass_1 = 100
mass_2 = 100
mass_3 = 100 

distance = 0
count = 0
G = 2e-10

m_sun = 3300000 #Is the ratio of earth to sun in actual space 2250000 
timestep = 1
orbit_choice = False

ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)

interface.mainloop        

