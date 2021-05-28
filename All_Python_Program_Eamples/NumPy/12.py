import numpy as np

# Broadcasting: When there is diffrent element size and diffrent array then go to the broadcasting concept

# a = np.array([[1,2,3],[2,4,6]]) #(2,3)
# b = np.array([1,6,3]) #(3,) then (1,3) then (2,3) at list np.array([1,6,3],[1,6,3])
# print(a+b)

a = np.array([1,1,5]) #(3,)
print(a.shape)
b = np.array([3,3,3]) #(3,)
print(b.shape)
print(a+b)