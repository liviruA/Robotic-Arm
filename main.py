#!/usr/bin/env python
# coding: utf-8

# In[11]:

import random
import time
import sys
sys.path.append('../')

from Common_Libraries.p2_sim_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        arm.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

arm = qarm()
update_thread = repeating_timer(2, update_sim)

#thresholds that will be used for activating the while loops
threshold  = 0.2
threshold2= 0.9 

#This function will identify a randomized number from a list from 1 to 6 and spawn the box with the certain ID on the spawn platform
def ID_X(x):
    '''
    Function name: ID_X

    Purpose: To spawn and identify the characteristics of the boxes which are spawned

    Inputs: a randomized number between 1 and 6
    Outputs: the colour and the size of the randomized number ID which was inserted

    Author: Liam Gleeson
    Last updated: December 04th, 2021
    '''
    if x == 1:
        arm.spawn_cage(1)
        colour_size = "red and small"

    if x == 2:
        arm.spawn_cage(2)
        colour_size = "green and small"

    if x == 3:
        arm.spawn_cage(3)
        colour_size = "blue and small"

    if x == 4:
        arm.spawn_cage(4)
        colour_size = "red and big"

    if x == 5:
        arm.spawn_cage(5)
        colour_size = "green and big"
        
    if x == 6:
        arm.spawn_cage(6)
        colour_size = "blue and big"

    return colour_size



#This function allows the user to open or close the red drawer. 
def drawerRED():
    global threshold2
    global threshold
    '''
    Function name: drawerRED

    Purpose: To open or close the red drawer

    Inputs:
    Outputs: The red drawer opens/closes

    Author: Noah Puskas
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_left())>threshold and float(arm.emg_right())<threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
                arm.open_red_autoclave(True)
    while float(arm.emg_left())<threshold and float(arm.emg_right())>threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
                arm.open_red_autoclave(False)
    
    
#This function allows the user to open or close the blue drawer.
def drawerBLUE():
    global threshold2
    global threshold
    '''
    Function name: drawerBLUE

    Purpose: To open or close the blue drawer

    Inputs: 
    Outputs: The blue drawer opens/closes

    Author: Liam Gleeson
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_left())>threshold and float(arm.emg_right())<threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
                arm.open_blue_autoclave(True)
    while float(arm.emg_left())<threshold and float(arm.emg_right())>threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
                arm.open_blue_autoclave(False)
    
    
#This function allows the user to open or close the green drawer.
def drawerGREEN():
    global threshold2
    global threshold
    '''
    Function name: drawerGREEN

    Purpose: To open or close the green drawer

    Inputs:
    Outputs: The green drawer opens/closes

    Author: Liviru Abeygunawardena
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_left())>threshold and float(arm.emg_right())<threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
                arm.open_green_autoclave(True)
    while float(arm.emg_left())<threshold and float(arm.emg_right())>threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
                arm.open_green_autoclave(False)
                
                
#this will position the Q-arm in a good position for picking up the box on the spawn platform     
def pickup():
    global threshold
    global threshold2
    '''
    Function name: pickup

    Purpose: To position the Q-arm in front of the box that is spawned

    Inputs:
    Outputs: move the Q-arm to a suitable position where it can pick up the box

    Author: Noah Puskas
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
        if float(arm.emg_right())<threshold and float(arm.emg_left())>threshold:
            arm.move_arm(0.5, 0, 0.04)
            
            
#this function will move the gripped box to the red bin and specific box position (top or drawer) according to the ID of the box
def move_end_effector_red(ID):
    global threshold
    global threshold2
    '''
    Function name: move_end_effector_red

    Purpose: To transport the two types of red boxes into their assigned postion in the bin

    Inputs: the ID of the box being picked up
    Outputs: move the Q-arm to the top or the bottom of the red bin

    Author: Liviru Abeygunawardena
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_left())>threshold and float(arm.emg_right())<threshold and ID == "red and small":
                arm.move_arm(-0.58, 0.23, 0.4)
            elif float(arm.emg_left())>threshold and float(arm.emg_right())<threshold and ID == "red and big":
                arm.rotate_shoulder(-45)
                time.sleep(1)
                arm.rotate_base(160)

        

        
#this function will move the gripped box to the blue bin and specific box position (top or drawer) according to the ID of the box     
def move_end_effector_blue(ID):
    global threshold
    global threshold2
    '''
    Function name: move_end_effector_blue

    Purpose: To transport the two types of blue boxes into their assigned postion in the bin

    Inputs: the ID of the box being picked up
    Outputs: move the Q-arm to the top or the bottom of the blue bin

    Author: Noah Puskas
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_left())>threshold and float(arm.emg_right())<threshold and ID == "blue and small":
                arm.move_arm(0, 0.63, 0.38)
            elif float(arm.emg_left())>threshold and float(arm.emg_right())<threshold and ID == "blue and big":
                arm.rotate_shoulder(-45)
                time.sleep(1)
                arm.rotate_base(90)


#this function will move the gripped box to the green bin and specific box position (top or drawer) according to the ID of the box
def move_end_effector_green(ID):
    '''
    Function name: move_end_effector_green

    Purpose: To transport the two types of green boxes into their assigned postion in the bin

    Inputs: the ID of the box being picked up
    Outputs: move the Q-arm to the top or the bottom of the green bin

    Author: Liviru Abeygunawardena
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_left())>threshold and float(arm.emg_right())<threshold and ID == "green and small":
                arm.move_arm(0, -0.64, 0.38)
            elif float(arm.emg_left())>threshold and float(arm.emg_right())<threshold and ID == "green and big":
                arm.rotate_shoulder(-45)
                time.sleep(1)
                arm.rotate_base(-90)

                
#This function will be used to bring the Q-arm back to its home position after dropping off boxes
def home():
    global threshold
    global threshold2
    '''
    Function name: home

    Purpose: To bring the Q-arm back to its home position after dropping off a box

    Inputs:
    Outputs: move the Q-arm back to its home position

    Author: Liam Gleeson
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
        if float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            arm.home()
            time.sleep(2)
    while float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
        if float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            arm.home()
            time.sleep(2)

            
#this function will close the grippers when needed
def control_gripper_close():
    global threshold
    global threshold2
    '''
    Function name: control_gripper_close

    Purpose: To close the gripper

    Inputs: 
    Outputs: closing the grippers of the Q-arm

    Author: Noah Puskas
    Last updated: December 04th, 2021
    '''
    while float(arm.emg_right())<threshold and float(arm.emg_left())>threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
                arm.control_gripper(30)

                
#this function will open the grippers when needed
def control_gripper_open():
    '''
    Function name: control_gripper_open

    Purpose: To open the gripper

    Inputs: 
    Outputs: opening the grippers of the Q-arm

    Author: Liviru Abeygunawardena
    Last updated: December 04th, 2021
    '''
    global threshold
    global threshold2
    while float(arm.emg_right())<threshold and float(arm.emg_left())>threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
                arm.control_gripper(-30)

    while  float(arm.emg_right())>threshold and float(arm.emg_left())>threshold:
        while float(arm.emg_right())<threshold2 and float(arm.emg_left())<threshold2:
            if float(arm.emg_right())>threshold and float(arm.emg_left())<threshold:
                arm.control_gripper(-30)




#This function will call each and every function above when needed     
def main():
    '''
    Function name: main

    Purpose: To properly operate the Q-arm according to the sensor data given. In addition to sort and spawn each and every box without repetition

    Inputs: 
    Outputs: The Q-arm being reponsive to each and every sensor command given

    Author: Liviru Abeygunawardena
    Last updated: December 04th, 2021
    '''
    boxIDs = [1, 2, 3, 4, 5, 6]
    #This loop allows the main function to only spawn a certain box once by selecting a random box from the boxIDs list
    for i in range (0,6):
        randnum = random.randint(0, len(boxIDs)-1)
        contID = boxIDs.pop(randnum)
        Id = ID_X(contID)
        if Id == "red and small":
            pickup()
            control_gripper_close()
            move_end_effector_red(Id)
            control_gripper_open()
            home()
        elif Id == "red and big":
            pickup()
            control_gripper_close()
            move_end_effector_red(Id)
            drawerRED()
            control_gripper_open()
            drawerRED()
            home()
        elif Id == "blue and small":
            pickup()
            control_gripper_close()
            move_end_effector_blue(Id)
            control_gripper_open()
            home()
        elif Id == "blue and big":
            pickup()
            control_gripper_close()
            move_end_effector_blue(Id)
            drawerBLUE()
            control_gripper_open()
            drawerBLUE()
            home()
        elif Id == "green and small":
            pickup()
            control_gripper_close()
            move_end_effector_green(Id)
            control_gripper_open()
            home()
        elif Id == "green and big":
            pickup()
            control_gripper_close()
            move_end_effector_green(Id)
            drawerGREEN()
            control_gripper_open()
            drawerGREEN()
            home()

# In[ ]:




