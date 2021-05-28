import numpy as np

# Advance Indexing

#1-D Array by advance indexing
#1st Way:

a =  np.array([10,20,30,40,50,60,70,80,90,200,100])
indexes = np.array([0,2,4,7]) #mentioned indexes
print(a[indexes])

#2nd Way:
''' directly passed indexes to list '''
print(a[[1,3,5,7]])
print("-"*100)
#---------------------------------------------------------------------------

# 2-D Array:
a = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16] ])
print(a)
print()
print(a[[0,1,2,3],[0,1,2,3]])
print(a[[1,3,2],[1,1,3]])
print("-"*100)
#---------------------------------------------------------------------------


# 3-D Array: accessing arbitrary element
a = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[21,22,23,24],[15,16,17,18],[29,310,311,212],[313,114,215,16]]])
print(a)
print()
#print(a[[Which_2D Array],[Row_index],[Column_index]])
print(a[[0,1],[0,0],[0,0]])
print(a[[0],[0,1,2,3],[0,1,2,3]])
print(a[[1],[0,1,2,3],[0,1,2,3]])
print(a[[0,1,0],[2,0,1],[1,3,2]])
print("-"*100)

#-----------------------------------------------------------------------------------------
# Conditional array
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[a>5])
print(a[a<=5])
