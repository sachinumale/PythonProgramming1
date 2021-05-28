import numpy as np

# Iterating element from array: 1. loop , 2. nditer , 3.ndenumerate
#-------------------------------------------------------------------
'''
1. By using loop: -
-------------------
1-D Array:
'''
# a = np.array([2,3,4,5,6,7,8,9])
# for x in a:
#     print(x)

#-------------------------------------------------
# 2-D Array:-
# a = np.array([[1,2,3],[4,5,6]])
# for x in a:
#     for y in x:
#         print(y)

#-------------------------------------------------
# 3-D Array:-

# a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[3,6,8]]])
# for x in a:
#     for y in x:
#         for z in y:
#             print(z)
#-------------------------------------------------

'''
2. nditer
------------
'''
# 1.D Array:-
# a = np.array([10,2,3,4,5,6,7,8,90])
# for x in np.nditer(a,flags =['buffered'],op_dtypes=['float']):
#     print(x)
#------------------------------------------------------------
# 2-D Array:-
# a = np.array([[1,22,3],[4,55,6]])
# for x in np.nditer(a[:,:2]):
#     print(x)
#--------------------------------------------------------------
# # 3-D Array:-
# a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[3,6,8]]])
# for x in np.nditer(a, flags=['buffered'],op_dtypes=['float']):
#     print(x)

'''
3. ndenumarater: gives element with indexes
'''
# 1-D Array:
# a = np.array([10,2,3,4,5,6,7,8,90])
# for x in np.ndenumerate(a):
#     print(x)
#------------------------------------------------------
#2-D Array:-
# a = np.array([[1,22,3],[4,55,6]])
# for x in np.ndenumerate(a[:,:1]):
#      print(x)

#-------------------------------------------------------
#--------------------------------------------------------------
# # 3-D Array:-
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[3,6,8]]])
for x in np.ndenumerate(a, flags=['buffered'],op_dtypes=['float']):
    print(x)