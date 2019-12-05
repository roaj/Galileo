import numpy as np
import time
import pysicktim as lidar
import L2_log as log
import L1_gamepad as gp
import L2_speed_control as sp_control
import L2_inverse_kinematics as inv_kin
import L1_motors as motor
import ball_seeker as bs
import gpio_galileo as gpio
count = 0
log.uniqueFile(count,"count.txt")

def vac_ON():
    gpio.vac_on()
    
def vac_OFF():
    gpio.vac_off()
    
def get_min(sweep_dis):                                 #input array from 0.4m sweep 
    min_sweep = sweep_dis.min()                         #get the smallest value of the array
    return(min_sweep)                                   #return smallest value
    
def get_distance():                                      #returns array 
    lidar.scan()                                	    # Requests and returns list of LiDAR
    	            	                                # distance data in meters
    scan_points = np.asarray(lidar.scan.distances)      # assign all points to scan_points
    sweep_dis = scan_points[300:500:1]                  # a = points on the array from 338 - 474
    return sweep_dis                                    #sweep_dis = 0.4 m sweep (distances)
    
def stop_mov():
    motor.MotorL(0)
    motor.MotorR(0)

#takes input from the gamepad and controls the scuttle
def manual_nav():
    c = inv_kin.getPdTargets()
    duties = sp_control.openLoop(c[0],c[1])
    motor.MotorL(duties[0])
    motor.MotorR(duties[1])
  
def autonomous_nav(min_angle):
    thetadot = get_thetadot(min_angle) #pass angle return theta_dot
    C = go_ball(thetadot) #[phi_dot_L , phi_dot_R]
    duties = sp_control.openLoop_ball(C[0],C[1])
    vac_ON()
    motor.MotorL(duties[0])
    motor.MotorR(duties[1])
    time.sleep(0.5)
    motor.MotorL(-.7)
    motor.MotorR(-.7)
    time.sleep(2)
    vac_OFF()
    
def ball_look():
    near_vector = bs.get_nearest() #return vector with the smallest distance [d,theta]
    min_distance = round(near_vector[0],3)
    # print(min_distance)
    
    if min_distance <= 0.365:
        min_angle = round(near_vector[1],3)
        #print("ball found")
        log.uniqueFile_2("Autonomous Mode","state.txt")
        global count
        count = count + 1
        log.uniqueFile(count,"count.txt")
        if min_angle < -15 or min_angle > 15 :
            autonomous_nav(min_angle)
        else:
            vac_ON()
            motor.MotorL(-.8)
            motor.MotorR(-.8)
            time.sleep(2)
            vac_OFF()
            
    elif min_distance > 0.37:
        motor.MotorL(0)#need to be taken out
        motor.MotorR(0)
        #print("no ball")
        log.uniqueFile_2("Manual Mode", "state.txt")
        pass
       
def get_thetadot(angle):
    time = 2 #seconds
    thetadot = angle/time
    return(thetadot)

def go_ball(thetadot):
    x_dot = 0
    B = np.array((x_dot,thetadot)) # B = [x_dot , theta_dot]
    C = inv_kin.convert(B) # C = [phi_dot_L , phi_dot_R]
    C = np.clip(C, -9.7, 9.7 )
    return(C)
    
def read_mqtt():
    mqtt = open("/home/debian/Galileo/power.txt","r") #server topi mxet300/galileo/power 
    mqtt_message = mqtt.read(1)
    mqtt.close()
    return(mqtt_message)
    
    
def go_ballSeeker():    #threading
    while 1:
        ball_look()
        
def go_nav():           #threading
    while 1:
        manual_nav()
    

def main():
    while 1:
        mqtt = read_mqtt()
        if mqtt == "1":
            log.uniqueFile_2("Galileo ON", "on_off.txt")
            ball_look()
            manual_nav()
        elif mqtt == "0":
            log.uniqueFile_2("Galileo OFF", "on_off.txt")
            log.uniqueFile_2(" ", "state.txt")
            time.sleep(1)
            pass
    

while 1:
  manual_nav()