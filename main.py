#==============================
#=== JOHNNY-5 ROBOT PROGRAM ===
#==============================
# Date: 08-04-2025
#==============================
# Author(s): Robot Group 3 
#==============================
#Desc: This Program Controls J-O-H-N-N-Y -5- as it performs dynamic 
#changes throughout a predetermined obstacle course.
#This program will run using pyhton in an IDE with version control using git.



#========
# Define required libraries.
#========
import time


#========
# Define required constants.
#========


#========
# Define Mode
#========
def start():
    # This must be the first line of any module that you write. It allows the chassis and the gimbal to move independently.
    robot_ctrl.set_mode(rm_define.robot_mode_free)


#========
# Set Speeds: 
#========
    # Set Rotate Speed: This sets the rotation speed of the gimbal.
    gimbal_ctrl.set_rotate_speed(60)

    # This next line sets the rotation speed for the bot itself rotating around using it's wheels.
    chassis_ctrl.set_rotate_speed(30)

    # set_trans_speed sets the movement speed of the robot in meters per second.
    chassis_ctrl.set_trans_speed(0.5)

    # Rotate with degree takes in a direction of rotation, and a number of degrees for the bot to rotate.
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # Recenter always rotates the gimbal back to its starting position of staring directly forward in front of it (yaw-wise), with a level pitch. Basically, it reset to 0, 0.
    gimbal_ctrl.recenter()

    # Yaw_ctrl rotates the gimbal by the number of degrees you pass into the function.
    gimbal_ctrl.yaw_ctrl(250)

    # Likewise, pitch_ctrl rotates the gimbal up and down by the number of degrees specified, in this case 15.
    gimbal_ctrl.pitch_ctrl(15)

#========
# Begin Here
#========

    # move_with_distance takes in two parameters, the first is an angle (0 meaning move straight ahead forward), and the second is a distance in meters
    # 
    # 
    #  (in this case, move 0.3 meters forward – the max distance is 5 meters - if you need to move more than 5 meters you need to set up two – or more – commands.)


    print("Johnny-5.0 is Moving To First Position.") # Would Be neat to put moving dots here . . . 
    chassis_ctrl.move_with_distance(0,0.3)
    time.sleep(1)

    print("Energy Support System Active, Navigation Systems are Syned.")
    print("Starting in:")

    for i in range(3,0,-1):
     print(i)
    time.sleep(1)
    print("Moving To First Target Area...")
    # This will move the robot 90 degrees in the right -- > direction also 0.81 meters
    chassis_ctr.move_with_distance(90,0.81)

    print("Area 1 is Clear.") # Message will disply when area is completed. 



#========
# 
#========



#========
# Phase 1: Approach - 16 forward 
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

   

