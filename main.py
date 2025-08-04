#==============================
#=== JOHNNY-5 ROBOT PROGRAM ===
#==============================
# Date: 08-04-2025
#==============================
# Author(s): Robot Group 3 
#==============================
#Desc: This is a program that allows the connected robot ( JOHNNY - 5 )
# JOHNNY-5 will perform dynamic movments throughout an obsticle course while being run via an IDE using Python.
# Version control using Git.
# The program will provide function to the robot and the output will be a dynamic rnage of movements
# that allows the robot to complete a predetermed course as per requirments.



#========
# Define required libraries.
#========



#========
# Define required constants.
#========


#========
# Define required functions.
#========
def start():
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    gimbal_ctrl.set-rotate_speed(60)

    chassis_ctrl.set_rotate_speed(30)

    chassis_ctrl.set_trans_speed(0.5)

    chassis_ctrl.move_with_distance(0,0.3)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    gimbal_ctrl.recenter()

    gimbal_ctrl.yaw_ctrl(250)

    gimbal_ctrl.pitch_ctrl(15)

#========
# Gather user inputs.
#========


#========
# Main program starts here.
#========



#========
# Perform required calculations.
#========
    

#========
# Display results
#========

    
#========
 # Write the values to a data file for storage.
#========


#========
# Any housekeeping duties at the end of the program.
#========

   

