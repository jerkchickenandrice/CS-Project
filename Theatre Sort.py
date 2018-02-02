# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:29:23 2017

@author: Family
"""
#Theatre

def add_seats(row):
    
i = 0
seat_num = 0
row_num = ['A','B','C','D','E','F','G','H','I','J']
allocated = []
row_chosen = 0
change_seat = False

while True:
    change_seat = False
    num_tickets = 0
    num_tickets = int(input("How many tickets are required"))
    
    while i < (num_tickets+seat_num):
        if (num_tickets + seat_num) > 15 :
            row_chosen = row_chosen + 1
            seat_assign = row_num[row_chosen] + str(i+1)
            print(seat_assign)
            allocated.append(seat_assign)
            i = i+1
            
        elif (num_tickets + seat_num) <= 15 :
            seat_assign = row_num[row_chosen] + str(i+1)
            print(seat_assign)
            allocated.append(seat_assign)
            i = i+1
        
         
        
        if i %15 == 0 :
            
            change_seat = True
            seat_num = 1
            row_chosen = row_chosen + 1    
            
    if change_seat == True :
        i = 0                         
            
    seat_num = i