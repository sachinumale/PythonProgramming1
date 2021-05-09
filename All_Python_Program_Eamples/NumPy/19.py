import numpy as np

# 1-D concatenate
a = np.arange(12)
b = np.arange(16,21)
c = np.concatenate((a,b))
print(c)
print("#"*200)

# 2-D concatenate
a1 = np.arange(9).reshape(3,3)
b1 = np.arange(12).reshape(4,3)
c1 = np.concatenate((a1,b1),axis=0)
print(c1)
print("*"*200)

# 3-D concatenate
a2 = np.arange(1,13).reshape(2,3,2)
b2 = np.arange(1,25).reshape(2,3,4)
c2 = np.concatenate((a2,b2),axis=2)
print(c2)


