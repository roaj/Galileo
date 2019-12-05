# This example drives the right and left motors.
# Intended for Beaglebone Blue hardware.
# This example uses rcpy library. Documentation: guitar.ucsd.edu/rcpy/rcpy.pdf
#!/usr/bin/env python3
import rcpy
import rcpy.motor as motor
import time # only necessary if running this program as a loop

motor_l = 1 	# Left Motor
motor_r = 2 	# Right Motor

rcpy.set_state(rcpy.RUNNING) # initialize the rcpy library

# define functions to command motors, effectively controlling PWM
def MotorL(speed): # takes argument in range [-1,1]
    motor.set(motor_l, speed)

def MotorR(speed): # takes argument in range [-1,1]
    motor.set(motor_r, speed)

# Uncomment this section to run this program as a standalone loop
# while rcpy.get_state() != rcpy.EXITING: # exit loop if rcpy not ready
#     if rcpy.get_state() == rcpy.RUNNING: # execute loop when rcpy is ready
#         print("L1_motors.py: driving fwd")
#         MotorL(0.6)  # gentle speed for testing program. 0.3 PWM may not spin the wheels.
#         MotorR(0.6)
#         time.sleep(4) # run fwd for 4 seconds
       