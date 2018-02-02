import tkinter
from tkinter import *

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
        
        #-------------Velocity In X-----------------
        vel_label=Label(self, text = 'Velocity X Planet 1')
        vel_label.grid(row=4,column=1)
        velocity_1 = Scale(self, from_=-42, to=42, orient = HORIZONTAL)
        velocity_1.grid(row=4, column=2)

        vel_label=Label(self, text = ' Velocity X Planet 2 ')
        vel_label.grid(row=4,column=3)
        velocity_2 = Scale(self, from_=-42, to=42, orient = HORIZONTAL)
        velocity_2.grid(row=4, column=4)

        vel_label=Label(self, text = ' Velocity X Planet 3 ')
        vel_label.grid(row=4,column=5)
        velocity_3 = Scale(self, from_=-42, to=42, orient = HORIZONTAL)
        velocity_3.grid(row=4, column=6)
        #-------------Velocity In Y-----------------
        vel_label=Label(self, text = 'Velocity Y Planet 1')
        vel_label.grid(row=5,column=1)
        velocity_1 = Scale(self, from_=-42, to=42, orient = HORIZONTAL)
        velocity_1.grid(row=5, column=2)

        vel_label=Label(self, text = ' Velocity Y Planet 2 ')
        vel_label.grid(row=5,column=3)
        velocity_2 = Scale(self, from_=-42, to=42, orient = HORIZONTAL)
        velocity_2.grid(row=5, column=4)

        vel_label=Label(self, text = ' Velocity Y Planet 3 ')
        vel_label.grid(row=5,column=5)
        velocity_3 = Scale(self, from_=-42, to=42, orient = HORIZONTAL, command = self.print_value())
        velocity_3.grid(row=5, column=6)
        #-------------Position------------------
        pos_label=Label(self, text = 'Position Planet 1')
        pos_label.grid(row=6, column=1)
        position_1 = Scale(self, from_=-100, to=100, orient=HORIZONTAL)
        position_1.grid(row=6,column=2)

        pos_label=Label(self, text = ' Position Planet 2 ')
        pos_label.grid(row=6, column=3)
        position_2 = Scale(self, from_=-100, to=100, orient=HORIZONTAL)
        position_2.grid(row=6,column=4)

        pos_label=Label(self, text = ' Position Planet 3 ')
        pos_label.grid(row=6, column=5)
        position_3 = Scale(self, from_=-100, to=100, orient=HORIZONTAL)
        position_3.grid(row=6,column=6)
        #-------------Mass--------------------
        mass_label=Label(self, text = 'Mass Planet 1')
        mass_label.grid(row=7,column=1)
        mass_1 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        mass_1.grid(row=7, column=2)

        mass_label=Label(self, text = ' Mass Planet 2 ')
        mass_label.grid(row=7,column=3)
        mass_2 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        mass_2.grid(row=7, column=4)

        mass_label=Label(self, text = ' Mass Planet 3 ')
        mass_label.grid(row=7,column=5)
        mass_3 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        mass_3.grid(row=7, column=6)

        

       

       # self.planet_one = BooleanVar()
        #Checkbutton(self,text="1", variable = self.planet_one, command = self.num_planets).grid(row=1,column=8,columnspan=1)
        
        #self.planet_two = BooleanVar()
        #Checkbutton(self,text="2", variable = self.planet_two, command = self.num_planets).grid(row=1,column=9,columnspan=1)
        
        #self.planet_three = BooleanVar()
        #Checkbutton(self,text="3", variable = self.planet_three, command = self.num_planets).grid(row=1,column=10,columnspan=1)

        
        
    def option_planet(self):
            
            if self.num_planet.get() == 1 :
                number_planet = 1
            if self.num_planet.get() == 2 :
                number_planet = 2
            if self.num_planet.get() == 3 :
                number_planet = 3
                
    def print_value(self):
        val = self.velocity_3.get()
        print(val)
            
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
            writing=Label(self, text = 'Start Animation')
            writing.grid(row=20,column=50)
    
                            
global number_planet
                            
interface = tkinter.Tk()
GUI = Simulator(interface)
Frame2 = Simulator 
interface.mainloop
