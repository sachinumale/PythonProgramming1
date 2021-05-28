import numpy as np

a = np.arange(1,13).reshape(4,3)
print(a)
for x in np.ndenumerate(a):
    print(x)