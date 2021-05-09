import numpy as np
import sys

# 1. zeros : help(np.zeros)

# a1=np.zeros((2,3,4),dtype=int)
# print(a1)
# print("-"*30)
# print("1. Shape",a1.shape)
# print("2. Dimentional",a1.ndim)
# print("3. Size",a1.size)
#---------------------------------------------------------------------------------------
# 2. ones : help(np.ones)
# a1=np.ones((3,2),dtype=int)
# print(a1)
# print("-"*30)
# print("1. Shape",a1.shape)
# print("2. Dimentional",a1.ndim)
# print("3. Size",a1.size)
#--------------------------------------------------------------------------------------

# 2. full : help(np.full(shape, fill_value, dtype=None, order='C', *, like=None))

# a1 = np.full((3,3),7)
# a2 = np.full((3,3),5,dtype=float)
# print(a1)
# print(a2)
# print("-"*30)
# print("1. Shape",a1.shape)
# print("2. Dimentional",a1.ndim)
# print("3. Size",a1.size)
#--------------------------------------------------------------------------------------



def get(a,b):
    c = a
    a = b
    b = c
    return a,b

a,b = get(2,3)
print(f"Before swapping a = 2 & b = 3")
print(f"After swapping  a = {a} & b = {b}")
















