from __future__ import annotations
import numpy as np
from quad import Quad


class Cuboid:
    
    def __init__(self, x, y, z, width, height, deepth, color=(1,0,0), divX = 0, divY = 0, divZ = 0) -> None:
        # div = number of cuts to each edge during division to quadlets
        self.divX = divX
        self.divY = divY
        self.divZ = divZ
        
        self.ppn = [] #projected_points_normalized
        self.pp = [] #projected points in canvas coordinates
        self.points = []
        self.points.append(np.array([x, y, z, 1]))
        self.points.append(np.array([x, y + height, z, 1]))
        self.points.append(np.array([x + width, y, z, 1]))
        self.points.append(np.array([x + width, y + height, z, 1]))
        self.points.append(np.array([x, y, z + deepth, 1]))
        self.points.append(np.array([x, y + height, z + deepth, 1]))
        self.points.append(np.array([x + width, y, z + deepth, 1]))
        self.points.append(np.array([x + width, y + height, z + deepth, 1]))

        self.color = color


    def getQuads(self) -> list[Quad]:
        color = self.color
        quads = []
        quads.append(Quad(np.array([self.points[0], self.points[1], self.points[3], self.points[2] ]), color=color, div0=self.divY, div1=self.divX ))
        quads.append(Quad(np.array([self.points[1], self.points[5], self.points[7], self.points[3] ]), color=color, div0=self.divZ, div1=self.divX))
        quads.append(Quad(np.array([self.points[3], self.points[7], self.points[6], self.points[2] ]), color=color, div0=self.divZ, div1=self.divY))
        quads.append(Quad(np.array([self.points[2], self.points[6], self.points[4], self.points[0] ]), color=color, div0=self.divZ, div1=self.divX))
        quads.append(Quad(np.array([self.points[0], self.points[4], self.points[5], self.points[1] ]), color=color, div0=self.divZ, div1=self.divY))
        quads.append(Quad(np.array([self.points[6], self.points[7], self.points[5], self.points[4] ]), color=color, div0=self.divY, div1=self.divX))
        return quads
    

    def applyTransformation(self, transformation:np.ndarray):
        for i, point in enumerate(self.points):
            tmp = transformation.dot(point)
            tmp = tmp/(tmp[3])
            self.points[i] = tmp
    


        