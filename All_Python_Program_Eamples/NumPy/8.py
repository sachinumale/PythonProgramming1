import numpy as np

# Accessing 1-D array

# a = np.array([10,20,30,40,50,60])
# print(a[0])
# print(a[4])

# Accessing 2-D array
# a = np.array([[10,20,30,40],[50,60,70,80]])
# print(a)
# print("Shape is:",a.shape)
# print(a[1][3])
# print(a[-1][-1])
# print(a[-1][3])
# print(a[1][-1])


# Accessing 3-D array
# [[1,2,3,4],[5,6,7,8]]
# [[9,10,11,12],[13,14,15,16]]
# a = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a[0][1][1])
# print(a[-1][1][1])

# Accessing 4-D array
# [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
# [[[11,12,13],[14,15,16],[17,18,19]],[[110,111,112],[113,114,115],[116,117,118]]]
# [[[21,22,23],[24,25,26],[27,28,29]],[[210,211,212],[213,214,215],[216,217,218]]]

a = np.array([[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]],[[[11,12,13],[14,15,16],[17,18,19]],[[110,111,112],[113,114,115],[116,117,118]]],[[[21,22,23],[24,25,26],[27,28,29]],[[210,211,212],[213,214,215],[216,217,218]]]])
print(a.shape)
print(a.ndim)
print(a)