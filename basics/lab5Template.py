# Lab5Template.py
# Team Number: 2
# Hardware TM: Joaquin Quireza
# Software TM: Jorge Roa
# Date: Oct 3
# Code purpose: Logs Heading angle into NodeRed
#NodeRed : https://gist.github.com/juacoq/b3c39ff4fb9ccb07cf48a512cd40aeca
# Import Internal Programs
import L2_log as log
import L2_heading as heading

# Import External programs
import numpy as np
import time

# DEFINE THE FUNCTIONS FOR THE PROGRAM
def task():
  
  axes = heading.getXY()
  axesScaled = heading.scale(axes)
  print(axesScaled)
  h = heading.getHeading(axesScaled)
  headingDegrees = round(h*180/np.pi,2) #converting raw data into degrees
  print("heading: ", headingDegrees) #printing value in terminal
  log.uniqueFile(headingDegrees,"headingDegrees.txt") #printing values in nodered
  log.uniqueFile(axesScaled[0], "scaledX.txt") #printing values in nodered
  log.uniqueFile(axesScaled[1], "scaledY.txt") #printing values in nodered
  
while 1:
    task()
    time.sleep(0.1) # delay a short period