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
    # Start setting for robot.
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    gimbal_ctrl.set_rotate_speed(60)
    
    chassis_ctrl.set_rotate_speed(30)
    
    chassis_ctrl.set_trans_speed(0.5)
    
    gimbal_ctrl.recenter()
    
    print("Johnny-5.0 is Moving To First Position.")
    
    chassis_ctrl.move_with_distance(0,5)
    time.sleep(1)
    chassis_ctrl.move_with_distance(0,0.85)
    
    time.sleep(5)

    print("Engery Support System Actice, Navigation Systems are Syned.")

def ZigZag():
    # Start of track.
    chassis_ctrl.move_with_distance(-90,0.85) # First turn to the left 90 degrees, go 31 inches.
    time.sleep(1)
    
    chassis_ctrl.move_with_distance(0,0.4) # Second move go forward 14 inches.
    time.sleep(1)
    
    chassis_ctrl.move_with_distance(90,1.75) # Third move go right 64 1/2 inches.
    time.sleep(1)
    
    chassis_ctrl.move_with_distance(0,0.48) # Forth move, go forward 16 1/2 inches.
    time.sleep(1)
    
    chassis_ctrl.move_with_distance(-90,0.6) # Fifth move, go left 90 degrees, 20 1/4 inches.
    time.sleep(4)
    
    chassis_ctrl.move_with_distance(-47,1.7) # Sixth move, go left 45 degrees, 58 1/2 inches.
    time.sleep(4)
    
    chassis_ctrl.move_with_distance(0, 0.3) # Seventh move, go straight, 20 inches.
    time.sleep(4)
    
    chassis_ctrl.move_with_distance(90, 0.9) # Eighth move, turn right 90 degrees, 33 inches.
    time.sleep(4)
    
    chassis_ctrl.move_with_distance(0, 0.35) # Nineth move, go forward 15 inches.
    time.sleep(4)