import numpy as np
W1=np.random.randn(2,4)
b1=np.random.randn(4)
x=np.random.randn(10,2)
h=np.dot(x,W1)+b1
print(h)