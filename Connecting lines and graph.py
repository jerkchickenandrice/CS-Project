from matplotlib import pyplot as plt  # Plots the points on a visual solution
from matplotlib import style          # Allows the aesthetics to be chosen
from matplotlib import animation as animation  #Animates an image by updating changes
import numpy as np # Arrays 
import math # manipulate complex mathematical functions
import tkinter  # The module that allows for GUI to be created
from tkinter import *
from decimal import *
import os # Access the system on the computer
number_planet = 1  # Initially the GUI displays a single set of widgets for a planet

class Simulator(Frame):

    def __init__(self,interface): # Initiator of the window 
        
        'Initialize the Frame'
        
        Frame.__init__(self, interface)
        interface.minsize(width = 1000, height = 500) # Sets the required sizes for the window 
        interface.maxsize(width = 1000, height = 500)
        interface.resizable(width=False, height=False) # The sizes cannot be changed as widgets may then become cluttered
        self.grid()  
        self.create_widgets() # Calls the method that creates the widgets
        
        
    def create_widgets(self):

        #Button function called and place chosen within the window. 
        Start_Sim_Button = Button(self, text="START", fg="green", command = self.start_orbit)
        Start_Sim_Button.grid(row=1,column=1,columnspan = 1)

        #Text that is shown to the user on the GUI 
        instruction = Label(self, text = "Number of Planets")
        instruction.grid(row=2,column=1,columnspan=1)

        #Set of buttons that allows for only 1 of the 3 to be selected at a time. 
        self.num_planet = IntVar() # The variable passed is an integer that corresponds to a condition within the command when the button is pressed
        Radiobutton(self, text="1", variable=self.num_planet, value=1, command = self.option_planet).grid(row=2, column = 2)
        Radiobutton(self, text="2", variable=self.num_planet, value=2, command = self.option_planet).grid(row=2, column = 3)
        Radiobutton(self, text="3", variable=self.num_planet, value=3, command = self.option_planet).grid(row=2, column = 4)
        
        # The parameters indicatoron is the type of radiobutton that is shown. It is different to the standard RadioButton
        orbit_choice = IntVar() # The variable passed is an integer that corresponds to a condition within the command when the button is pressed
        Radiobutton(self,text='Orbital Paths?', indicatoron = 0, width = 15,variable=orbit_choice, command=self.orb_path , value=1).grid(row = 1, column =2)

        #Button that opens the instruction file 
        open_instructions = Button(self, text="Instructions", fg = 'magenta' , command = self.open_instructions)
        open_instructions.grid(row=1 ,column =4)

        #Button that saves the selected variables that are temporarily chosen within the GUI
        save_variables_button = Button(self, text = 'Save Variables', fg = 'blue', command = self.save_variables)
        save_variables_button.grid(row=1,column=3)

        #Button that explains the forces in action with regards to planetary orbits
        explain_plots = Button(self, text = 'Explain Physics', fg = '#0099FF#', command = self.explain_physics)
        explain_plots.grid(row=1,column=5)
        
        #-------------Velocity In X-----------------
        #Creating sliders for each variable within the GUI and then duplicating the code and changing the varriables to correspond to a different planet
        
        vel_label=Label(self, text = 'Velocity X Green Planet')
        vel_label.grid(row=4,column=1)
        velocityX_1 = Scale(self, from_=-10, to=10, orient = HORIZONTAL , command = self.vel_x_1, resolution = 0.1) # Horizontal slider, resolution is increment of the slider when moved one place
        velocityX_1.grid(row=4, column=2)

        if number_planet == 2 or number_planet == 3: # The integer variable which only creates widgets based on how many planets to user would like to use
            
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
        mass_1 = Scale(self, from_=0, to=3000, orient=HORIZONTAL, command = self.mass_1)
        mass_1.grid(row=7, column=2)

        if number_planet == 2 or number_planet == 3:
        
            mass_label=Label(self, text = ' Mass of Purple Planet')
            mass_label.grid(row=7,column=3)
            mass_2 = Scale(self, from_=0, to=3000, orient=HORIZONTAL,command = self.mass_2)
            mass_2.grid(row=7, column=4)
        
        if number_planet == 3 :
            
            mass_label=Label(self, text = ' Mass of Red Planet')
            mass_label.grid(row=7,column=5)
            mass_3 = Scale(self, from_=0, to=3000, orient=HORIZONTAL, command = self.mass_3)
            mass_3.grid(row=7, column=6)

        #self.planet_one = BooleanVar()
        #Checkbutton(self,text="1", variable = self.planet_one, command = self.num_planets).grid(row=1,column=8,columnspan=1)
        
        #self.planet_two = BooleanVar()
        #Checkbutton(self,text="2", variable = self.planet_two, command = self.num_planets).grid(row=1,column=9,columnspan=1)
        
        #self.planet_three = BooleanVar()
        #Checkbutton(self,text="3", variable = self.planet_three, command = self.num_planets).grid(row=1,column=10,columnspan=1)

    def save_variables(self):
        #Splits each variables into a preset title with the string value of the variables so that they can be written to a text file without any type errors
        file = open("Simulation_Variables.txt","w+") # w+ indicated that we are intending to write to a text file. 
        file.write("Velocity X Green Planet = " + str(vel_x_1*100) + "   Velocity X Purple Planet = " + str(vel_x_2*100) + "   Velocity X Red Planet = " + str(vel_x_3*100)+ "\n")
        file.write("Velocity Y Green Planet = " + str(vel_y_1*100) + "   Velocity Y Purple Planet = " + str(vel_y_2*100) + "   Velocity Y Red Planet = " + str(vel_y_3*100)+ "\n")
        file.write("Position Green Planet   = " + str(x_pos_1[0])  + "   Position Purple Planet   = " + str(x_pos_2[0]) +  "   Position Red Planet   = " + str(x_pos_3[0])+ "\n")
        file.write("Mass of Green Planet    = " + str(mass_1)      + "   Mass of Purple Planet    = " + str(mass_2) +      "   Mass of Red Planet    = " + str(mass_3)+ "\n")
        
    def option_planet(self):
            #This methods sets the variable number_planet and calls the function which recreates the GUI when a different radiobutton is pressed
            global number_planet # This variable will be utilised within the subroutines for determining planets orbits. 
            
            if self.num_planet.get() == 1 :
                number_planet = 1
            if self.num_planet.get() == 2 :
                number_planet = 2
            if self.num_planet.get() == 3 :
                number_planet = 3
            self.create_widgets() # The function with all of the buttons and sliders etc. 
            
    def orb_path(self):
        # Allows for trails to occur by setting the boolean to True. Using the RadioButtons
        global orbit_choice
        orbit_choice = True

    def open_instructions(self):
        #Utilising the Module os to allow for the file to be ddisplayed to the user instantly.
        os.startfile("Orbit_Instructions.txt")
                        
    def vel_x_1(self,tempval):
        #Value of velocity in the x direction for planet 1.
        #All variables used to represent the planets have to be globalised in order to be used in later subroutines
        global vel_x_1
        vel_x_1 = Decimal(tempval)/Decimal(100) #Normalise the vector so that the speed doesn't increase exponentially. 
        
    def vel_x_2(self,tempval):
        #Value of velocity in the x direction for planet 2
        global vel_x_2
        vel_x_2 = Decimal(tempval)/Decimal(100)
        
    def vel_x_3(self,tempval):
        #Value of velocity in the x direction for planet 3
        global vel_x_3
        vel_x_3 = Decimal(tempval)/Decimal(100)
    
    def vel_y_1(self,tempval):
        #Value of velocity in the y direction for planet 1
        global vel_y_1
        vel_y_1 = Decimal(tempval)/Decimal(100)
        
    def vel_y_2(self,tempval):
        #Value of velocity in the y direction for planet 1
        global vel_y_2
        vel_y_2 = Decimal(tempval)/Decimal(100)
    
    def vel_y_3(self,tempval):
        #Value of velocity in the y direction for planet 1
        global vel_y_3
        vel_y_3 = Decimal(tempval)/Decimal(100)
        
    def position_1(self,tempval):
        #Value of Position for planet 1
        global position_1
        position_1 = Decimal(tempval)
        x_pos_1[0] = (position_1)
        
    def position_2(self,tempval):
        #Value of Position for planet 2
        global position_2
        position_2 = Decimal(tempval)
        x_pos_2[0]=(position_2)

    def position_3(self,tempval):
        #Value of Position for planet 3
        global position_3
        position_3 = Decimal(tempval)
        x_pos_3[0]=(position_3)
    
    def mass_1(self,tempval):
        #Value of Mass for planet 1
        global mass_1
        mass_1 = int(tempval) # Integer values used here because the mass is never a decimal due to the way the sliders are coded
        
    def mass_2(self,tempval):
        #Value of Mass for planet 1
        global mass_2
        mass_2 = int(tempval)
    
    def mass_3(self,tempval):
        #Value of Mass for planet 1
        global mass_3
        mass_3 = int(tempval)
        

    
    def num_planets(self):
        # Test to utilise the use of Radiobuttons while developing the programs.
        #  Although redunant, May be of use in the future to developers
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
            # The start button goes here and begins the infinite animation function call which it will never break out of.
            ani = animation.FuncAnimation(fig, animate, interval = 10) #A class functions which loops the drawing of the chart
            plt.show()
    
    def explain_physics(self):
        #Utilising the Module os to allow for the file to be ddisplayed to the user instantly.
        os.startfile("Explain_Physics.txt")

def animate(i): # The function animate automatically called the subroutine with name animate. Parameter i is passed.
    global number_planet
    global count
    
    def planet_1(): #The subroutine responsible for the processing of planet 1
        global distance
        global vel_y_1
        global vel_x_1
        global G
        
        distance = (x_pos_1[count])**2 +(y_pos_1[count])**2
        sqrt = Decimal(distance)**Decimal(0.5) # All values that are passed as Decmials are put into decimal objects to be manipulated mathematically
        F = Decimal(G * mass_1 * m_sun) / Decimal(sqrt)**Decimal(2) # Must be Decimal objects to make computation possible 
        dirX = Decimal(-x_pos_1[count]) # Direction vector from 0,0 to the planet x,y
        dirY = Decimal(-y_pos_1[count]) # # Direction vector from 0,0 to the planet x,y
    
        Vec_magnitude  = (Decimal(dirX)**Decimal(2) + Decimal(dirY)**Decimal(2))**Decimal(0.5) #Size of the vector in terms of resultant force
    
        Fx = dirX * (F / Vec_magnitude) # Scales the magnitude and normalises the vector so that the planet doesnt build up a huge acceleration
        Fy = dirY * (F / Vec_magnitude)
     
        x_tem_pos = x_pos_1[count] + Decimal(vel_x_1) #Temporary variables which holds the position within the iteration
        y_tem_pos = y_pos_1[count] + Decimal(vel_y_1) #Makes debugging easier as it is clear what is happening with regards to manipulation of variables
        
        if orbit_choice == True : # Determines whether orbital plots are going to be sown based on the user's earlier inputs. 
            x_pos_1.append(x_tem_pos) # Adds the position to the end of the list
            y_pos_1.append(y_tem_pos)
        else :
            x_pos_1[0] = x_tem_pos # Constantly replaces the first element in the list with the temporary position to imitate a moving planet
            y_pos_1[0] = y_tem_pos
        
        Acc_x = Fx / mass_1 # Applying Newtons laws of orbital acceleration F = ma
        Acc_y = Fy / mass_1
    
        vel_x_1 = Decimal(Acc_x) + Decimal(vel_x_1) # Determining the value of velocity for the next iteration of the subroutine
        vel_y_1 = Decimal(Acc_y) + Decimal(vel_y_1)
        
        
        ax1.clear() # Clears the axis so that a new plot can be shown on each iteration. Necessary for animation orbits
        
        if orbit_choice == True : # To do with orbital trails.
            ax1.plot(x_pos_1, y_pos_1, '-o', markersize=1.0 , color = 'C0') # Plots a line graph connecting al the points where the planet has been
        else:    
            ax1.scatter(x_pos_1,y_pos_1, s = 0.5, color = 'C0')#Scatter a single point on the axis. Constantly updating.
        
        
        ax2.scatter(0, 0, color ='C1') # The points on the axis that represents the central Sun
        ax1.get_xaxis().get_major_formatter().set_scientific(False) # Turns off sceintific saling to have whole numbers only
        

    def planet_2():
        #Identical copy of the subroutine Planet_1 with the variables instead representing planet_2. Simple duplication of code
        #Possible future development to be able to loop them all through a single subroutine. However for now this works
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
        
        if orbit_choice == True :
            x_pos_2.append(x_tem_pos)
            y_pos_2.append(y_tem_pos)
        else :
            x_pos_2[0] = Decimal(x_tem_pos)
            y_pos_2[0] = Decimal(y_tem_pos) 
    
        Acc_x = Fx / mass_2
        Acc_y = Fy / mass_2
    
        vel_x_2 = Decimal(Acc_x) + Decimal(vel_x_2)
        vel_y_2 = Decimal(Acc_y) + Decimal(vel_y_2)
        

        if orbit_choice == True :  
            ax1.plot(x_pos_2, y_pos_2,markersize=1.0, color = 'C2')
        else:    
            ax1.scatter(x_pos_2,y_pos_2, s = 2, color = 'C2')

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

        if orbit_choice == True :
            x_pos_3.append(x_tem_pos)
            y_pos_3.append(y_tem_pos)
        else :
            x_pos_3[0] = Decimal(x_tem_pos)
            y_pos_3[0] = Decimal(y_tem_pos)
            
            
        Acc_x = Fx / mass_3
        Acc_y = Fy / mass_3
    
        vel_x_3 = Decimal(Acc_x) + Decimal(vel_x_3)
        vel_y_3 = Decimal(Acc_y) + Decimal(vel_y_3)

        if orbit_choice == True :  
            ax1.plot(x_pos_3, y_pos_3,markersize=1.0, color = 'C3')
        else:    
            ax1.scatter(x_pos_3,y_pos_3, s=2, color = 'C3')
        
        ax2.scatter(0, 0, color ='C1')
        ax1.get_xaxis().get_major_formatter().set_scientific(False)
        
    #The subroutine called when the animation function is called. This is on an endless loop and depends on how many planets the user has chosen to use.
    planet_1()
    if number_planet == 2 or number_planet ==3:
        planet_2()
    if number_planet == 3:
        planet_3()
    if orbit_choice == True :
        count = count + 1 # Count is only used for when orbit choice is used due to the position of variables within a list.
         
    ax1.set_xlim([-5.5,5.5]) # The limits of each axis. Set to 5.5 after testing as it is valid for the plots that the user can create 
    ax1.set_ylim([-5.5,5.5])  
    ax1.set_title('Orbital Simulation') # Title shown on the simulation above the plot
    ax1.set_ylabel('Vertical Distance from Sun') # Y axis text
    ax1.set_xlabel('Horizontal Distance from Sun') # X axis text 

    
interface = tkinter.Tk() # Initialising the interface by creating a Tkiner mainloop 
GUI = Simulator(interface) # Not necessary but allows frames to be used in future development
Frame2 = Simulator
   
#Variables and Lists

style.use('dark_background')
fig = plt.figure() # Declares all elements to do with 'figure' to be displayed on the same single plot.
#Intialsing all of the variables to be used within the simulation within the mainloop of the tkinter GUI.
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
G = 6.67e-11 # The value of the Gravitational constant 2e-10

m_sun = 3300000 # the ratio of earth to sun in actual space 
orbit_choice = False

ax1 = fig.add_subplot(1,1,1) #Enables one to manipulate individual aspects of the figure/
ax2 = fig.add_subplot(1,1,1)            

interface.mainloop # Stops the windows from closing immediately and states that it must be looped

