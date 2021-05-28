import numpy as np

# a = np.arange(1,13).reshape(3,2,2)
# print(a)
# a1=np.transpose(a,axes=(1,0,2))
# print(a1)

b = np.arange(1,13).reshape(4,3)
print(b)
b1 = np.swapaxes(b,1,0)
print(b1)