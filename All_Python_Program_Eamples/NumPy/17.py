import numpy as np

# 1-D array:
#
# a = np.arange(1,12)
# b = a.flatten()
# print(b)

# 2-D array:
# a = np.arange(1,17).reshape(4,4)
# b = a.flatten()
# print(b)

# 3-D array:-

# a = np.arange(1,19).reshape(3,2,3)
# print(a)
# b1 = a.flatten()
# print(b1)

#----------------------------------------------------------------------
# ravel():-

a = np.arange(1,13).reshape(4,3)
# b1 = a.ravel()
# print(b1)
# b1[5]=999
# print(a)
print(a)
b = np.ravel(a,order='F')
print(b)


