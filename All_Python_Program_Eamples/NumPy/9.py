import numpy as np

# 1-D array Slicing
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a[1:5])
# print(a[1:5:-1])
# print(a[:-1:-1])

# 2-D Array Slicing
# a = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12]  ])
# print(a)
# print("--------Example-------")
# print(a[1:2,:])
# print(a[:,1:2])
# print(a[::2,::3])
# print(a[::2,::])

# 3-D array Slicing

a = np.array([[[1,2,3],[4,5,6],[5,4,3]],[[7,8,9],[10,11,12],[13,14,15]]])
print(a)
print("-------Example-----------")
print(a[:1,:,1:2])
print(a[:,::2,::2])
print(a[:,:,2:])
print(a[1:,2:,:])



