from quad import Quad
from cuboid import Cuboid
import numpy as np

#q = Quad([np.array([-1, 1, 2]), np.array([-4, 2, 2]), np.array([-2, 1, 5])] ,[np.array([-1, 1, 2]), np.array([-4, 2, 2]), np.array([-2, 1, 5])] )

#print(q.points)
#print(q.getMaxZ())
#print(q.getMinZ())

p = [np.array([-1, 1, 2]), np.array([-4, 2, 2]), np.array([-2, 1, 5])]

a = p[1] - p[0]
print(a)
b = p[2] - p[0]
print(b)
n = np.cross(a,b)
print(n)
print(n * -1)
d = np.dot(p[0],n)
print(d)

n = np.cross(b,a)
print(n)
d = np.dot(p[0],n)
print(d)




#print(10e-3)




