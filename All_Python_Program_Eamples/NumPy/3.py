import numpy as np
import sys
from datetime import datetime

#help(np.array)
#1-D Array
'''
a = np.array([10,20,30])
print(type(a))
print(a)
'''
#-----------------------------------
#2-D Array
'''
a = np.array([[10,20,30,40],[50,60,70,80]])
print(a)
print("Dimentaionla of Arry Is: ",a.ndim)
'''

#-----------------------------------
#3-D Array
'''
a = np.array([[[10,20],[30,40]],[[50,60],[70,80]],[[1,23],[3,4]]])
print(a)
print("Dimentaionla of Arry Is: ",a.ndim)

'''

#-----------------------------------
# Object daya type
'''
a1 = np.array([1,'Shri',True,11+7j,11.5],dtype=object)
print(a1)
print(type(a1))
print(a1.dtype)
'''
#-----------------------------------

# arange()

# a = np.arange(10)
# a = np.arange(1,10)
# a = np.arange(1,10,2)
# a = np.arange(1,10,2,dtype=float)
# print(a)

#-----------------------------------

# linespace

a1 = np.linspace(1,2,50)
print(a1)










