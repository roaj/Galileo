# Import pysicktim library as "lidar"
import pysicktim as lidar
import numpy as np
import L2_log as log

# Repeat code nested in for loop 10 times
for x in range(1):
# while True:

	lidar.scan()	# Requests and returns list of LiDAR
			# distance data in meters
	
	scan_points = np.asarray(lidar.scan.distances)
	a = scan_points[338:474:1]
	log.csv_write(a)
	print("sum is",a.sum())
	print("std is",np.std(a))
	
	# print distance list
	