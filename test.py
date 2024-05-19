#from quad import Quad
#from cuboid import Cuboid
import numpy as np
import colorsys

#q = Quad([np.array([-1, 1, 2]), np.array([-4, 2, 2]), np.array([-2, 1, 5])] ,[np.array([-1, 1, 2]), np.array([-4, 2, 2]), np.array([-2, 1, 5])] )

#print(q.points)
#print(q.getMaxZ())
#print(q.getMinZ())
"""
p = [np.array([-1, 1, 2]), np.array([-4, 2, 2]), np.array([-2, 1, 5])]

a = p[1] - p[0]
print(a)
b = p[2] - p[0]
print(b)
n = np.cross(a,b)
print(n)
d = np.dot(p[0],n)
print(d)

n = np.cross(b,a)
print(n)
d = np.dot(p[0],n)
print(d)
"""

a = np.array([[  0.17533083, -43.76838351,  91.08755644],
 [ -7.09275889, -28.13422175,  80.95109464],
 [  9.46701177, -27.7016379,   69.74454   ], 
 [ 16.73510149, -43.33579966,  79.88100181]])


#print(np.sqrt(np.dot(a[0],a[0])))
#print(10e-3)

b = np.array([1,2,3])
print(b)
b = np.append(b, 4)
print(b)



