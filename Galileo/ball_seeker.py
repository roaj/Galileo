import numpy as np
import time
import sys
import math
import Galileo_lidar as lidar
import L2_log as log
import L2_inverse_kinematics as inv_kin
import L2_vector as vector



def get_dy(d,thetha):
    
    dis_scan = d
    angles = np.deg2rad(thetha)
    x = len(dis_scan)
    dy = np.zeros(x)
    for i in range(x):
        dy[i] = np.cos(angles[i])*dis_scan[i]
        i += 1
    return dy


def get_nearest():
    
    scan = lidar.polarScan(811) #gets 811 scans [m,thetha]        
    scan_galileo = scan [334:478:1] #narrow the view 
    d = scan_galileo [:,0] #get the first column of the scan
    thetha = scan_galileo[:,1] #get the second column of the scan
    thetha = np.reshape(thetha,(thetha.shape[0],1)) #turn thetha into columumn
    dy = get_dy(d,thetha) #get vertical distance from the lidar to floor
    dy_reshape = np.reshape(dy,(dy.shape[0],1)) #turn dy into a column
    column_mins = np.argmin(dy,axis=0) #get the min index with the min dy value
    row_index = column_mins 
    scan_converted = np.hstack((dy_reshape,thetha)) #stack vertically [dy,thetha]
    nearest_element = scan_converted[row_index,:] #return the distance and angle of the nearest object in scan [dy_min, thetha]
    return (nearest_element)
    
