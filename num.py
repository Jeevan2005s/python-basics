import numpy as np
b=np.array([1,2,3,4,5,6,7,8])
c=b.reshape(-1,2)
# print(b.shape)
# print(c.shape)
c=np.zeros((3,2),dtype=int)
# print(c)
c=np.array(range(16),dtype=float)
c=c+0.5
# print(c[3])
x=c.astype(dtype=int)
# print(x)
# print(x[2:6])
# print(x[x%2==0])
s=x.reshape(4,4)
# print(s)
# print(len(s))
# print(len(s[0]))
a=[1,2,3,4]
# print(len(a))
# print(len(a))
a=np.arange(1,6,0.5)
print(a)