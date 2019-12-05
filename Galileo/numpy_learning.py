import numpy as np
import time
import sys
#import L1_lidar as lidar


a = np.array ((1,2))
print (a)
#convert to a single column

# print(np.ravel(a)) # making array 'a' into a single COLUMN











###Operations

# a = np.array ([(1,2,3),(4,5,6)])
# b = np.array([(8,9,10),(4,5,6)])

# operations
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

#concatinate arrays
# print(np.vstack((a,b))) #V - vertical / H - horizontal # 'a' on top of 'b'
# print(np.hstack((a,b))) #'a' of the right of 'a'


######### Axis concepts

    ### axis 0 = columns
    ### axis 1 = rows
    ### can use STD or SQR
# a = np.array([(1,2,3),(4,5,6)])
# print(a.sum(axis=0))
# print(np.sqrt(a)) #square root
# print(np.std(a)) #how much each element deviates from the mean of the array


###### getting lidar

# lidar_data = lidar.polarScan(20)
# print (lidar_data.size)

######  min max sum 

# a = np.array([(1,2,3), (4,5,6)])

# print(a.max()) #print largest number in array
# print(a.min()) #prints smallest number in the aray 
# print(a.sum()) #adds all the menber of the whole array


####### making arrays 

# a = np.linspace(1,3,5) # produces an array os 5 items, evenly distributed from 1 to 3
# print (a)


####### Particular element of the arrays


# a = np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12)])

# print(a[0,2])   # if i wanted to chose the third elemnt of the first array
#                 # indexing works by ELEMENTS there is two ELEMENTS on 'a', 
#                 # ELEMENT 0 and 1. 
                
# print (a[0:,3])   #I want to print 4 and 8 
#                 # [0:] = all the rows including 0
#                 # [0:,3] = in that row I want only index 3
                
#                     #if I want just 4 and 6 I cant do the previous becuse will also print 12
# print (a[0:2,3])    #  It wont include the second element (3rd row)        
                



######## reshaping = change the number of row and columns

# a = np.array([(1,2,3,4), (5,6,7,8)])
# print(a.shape)
# a = a.reshape(4,2)
# print(a.shape)



#########  size and shape

# a = np.array([(1, 2, 3) , (4, 5, 6)]) # each () is a element of the array 

# print(a.size) #prints number of elements in the array 
# print(a.shape) #prints the number of rows,columns
# print(a)


########### 

# a = np.array([(1,2,3) , (4,5,6)])

# print(a.ndim) # dimension
# print(a.itemsize)#each element size
# print(a.dtype)#data type

################### faster than list

# SIZE = 100000

# L1 = range (SIZE)
# L2 = range (SIZE)

# A1 = np.arange(SIZE)
# A2 = np.arange(SIZE)

# start = time.time()

# result = [(x,y) for x,y in zip(L1,L2)]
# print((time.time()-start)*1000)

# start = time.time()

# result = A1+A2

# print((time.time()-start)*1000)


################### size of array
# s = range(1000)

# print (sys.getsizeof(5)*len(s))

# D = np.arange(1000)

# print(D.size*D.itemsize)

################# initial

# a = np.array([(1,2,3) , (4,5,6)])

# print(a)