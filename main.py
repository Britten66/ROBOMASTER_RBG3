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
    # This must be the first line of any module that you write. It allows the chassis and the gimbal to move independently.
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    # Set Rotate Speed: This sets the rotation speed of the gimbal.
    gimbal_ctrl.set-rotate_speed(60)

    # This next line sets the rotation speed for the bot itself rotating around using it's wheels.
    chassis_ctrl.set_rotate_speed(30)

    # set_trans_speed sets the movement speed of the robot in meters per second.
    chassis_ctrl.set_trans_speed(0.5)

    # move_with_distance takes in two parameters, the first is an angle (0 meaning move straight ahead forward), and the second is a distance in meters (in this case, move 0.3 meters forward – the max distance is 5 meters - if you need to move more than 5 meters you need to set up two – or more – commands.)
    chassis_ctrl.move_with_distance(0,0.3)

    # Rotate with degree takes in a direction of rotation, and a number of degrees for the bot to rotate.
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # Recenter always rotates the gimbal back to its starting position of staring directly forward in front of it (yaw-wise), with a level pitch. Basically, it reset to 0, 0.
    gimbal_ctrl.recenter()

    # Yaw_ctrl rotates the gimbal by the number of degrees you pass into the function.
    gimbal_ctrl.yaw_ctrl(250)

    # Likewise, pitch_ctrl rotates the gimbal up and down by the number of degrees specified, in this case 15.
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

   

