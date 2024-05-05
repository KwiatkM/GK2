from functools import total_ordering
import numpy as np
from tkinter import Canvas

#@total_ordering
class Quad:
    
    def __init__(self, points3D:np.ndarray, pp:np.ndarray,  color='red') -> None:
        # points3D = 4 points (in order) in camera coordinates that form a quad
        # for each point: 
        #   first element = x
        #   second element = y
        #   third element = z
        self.points3D = points3D
        self.pp = pp
        self.color = color
        self.normal = np.cross(points3D[1] - points3D[0],points3D[3] - points3D[0])
        self.d = np.dot(points3D[0], self.normal)
        if self.d < 0:
            self.normal = self.normal * -1
            self.d = self.d * -1
        self.maxz = self.getMaxZ()

    def getMaxZ(self) -> float:
        zmax = -999.9
        for p in self.points3D:
            if p[2] > zmax:
                zmax = p[2]
        return zmax

    def getMinZ(self)-> float:
        zmin = 999999.9
        for p in self.points3D:
            if p[2] < zmin:
                zmin = p[2]
        return zmin
    
    def getProjectedMaxX(self) -> float:
        xmax = -999999.9
        for p in self.pp:
            if p[0][0] > xmax:
                xmax = p[0][0]
        return xmax

    def getProjectedMinX(self)-> float:
        xmin = 9999999.9
        for p in self.pp:
            if p[0][0] < xmin:
                xmin = p[0][0]
        return xmin
    
    def getProjectedMaxY(self) -> float:
        ymax = -999999.9
        for p in self.pp:
            if p[1][0] > ymax:
                ymax = p[1][0]
        return ymax

    def getProjectedMinY(self)-> float:
        ymin = 9999999.9
        for p in self.pp:
            if p[1][0] < ymin:
                ymin = p[1][0]
        return ymin

    def isPointInFront(self, point:np.ndarray):
        t = np.dot(self.normal, point) - self.d
        if abs(t) < 10e-3: return True
        return t > 0 
    
    def isPointBehind(self, point:np.ndarray):
        t = np.dot(self.normal, point) - self.d
        if abs(t) < 10e-3: return True
        
        return t < 0

    
    
    def draw(self, canvas:Canvas):
        canvas.create_polygon(self.pp[0][0][0], self.pp[0][1][0],
                              self.pp[1][0][0], self.pp[1][1][0],
                              self.pp[2][0][0], self.pp[2][1][0],
                              self.pp[3][0][0], self.pp[3][1][0],
                              fill=self.color)
        canvas.create_line(self.pp[0][0][0], self.pp[0][1][0], self.pp[1][0][0], self.pp[1][1][0], fill='black', width=1)
        canvas.create_line(self.pp[1][0][0], self.pp[1][1][0], self.pp[2][0][0], self.pp[2][1][0], fill='black', width=1)
        canvas.create_line(self.pp[2][0][0], self.pp[2][1][0], self.pp[3][0][0], self.pp[3][1][0], fill='black', width=1)
        canvas.create_line(self.pp[3][0][0], self.pp[3][1][0], self.pp[0][0][0], self.pp[0][1][0], fill='black', width=1)
    
    #def __lt__(self,other) -> bool:
    #    return self.isFurtherThan(other)

    def test(self, other):
        if self.getMinZ() >= other.getMaxZ(): return True
        if self.getMaxZ() <= other.getMinZ(): return False

        
        i=0
        for p in other.points3D:
            if (np.dot(self.normal, p) - self.d > 0) == self.front or np.dot(self.normal, p) - self.d == 0: i += 1
        if i == 4:return True
        if i == 0:return False

        i=0
        for p in self.points3D:
            if (np.dot(other.normal, p) - other.d > 0) == other.front or np.dot(other.normal, p) - other.d == 0: i += 1
        if i == 4:return False
        if i == 0:return True

        print('error: order of two quads cannot be calculated!')
        print(self)
        print(other)
        return False

    def isCloserThan(self,other) -> bool:
        if round(self.getMaxZ(),3) <= round(other.getMinZ(), 2): return True
        if round(self.getMinZ(),3) >= round(other.getMaxZ(), 2): return False


        
        f1 = 0
        b1 = 0
        for p in other.points3D:
            if self.isPointInFront(p):
                f1 += 1
            if self.isPointBehind(p):
                b1 += 1
        if f1 == 4: return True
        if b1 == 4: return False

        f2 = 0
        b2 = 0
        for p in self.points3D:
            if other.isPointInFront(p):
                f2 += 1
            if other.isPointBehind(p):
                b2 += 1
        if f2 == 4: return False
        if b2 == 4: return True

        print('error: order of two quads cannot be calculated!')
        print('Quad 1: ' + self.color)
        print(self.points3D)
        print('Normal vector: ' + str(self.normal) + ', d=' + str(self.d))
        print('Point 0 of quad 2 in front of quad 1? ' + str(self.isPointInFront(other.points3D[0])))
        print('Point 0 of quad 2 in behind quad 1? ' + str(self.isPointBehind(other.points3D[0])))
        print('\n')
        print('Quad 2: ' + other.color)
        print(other.points3D)
        print('Normal vector: ' + str(other.normal) + ', d=' + str(other.d))
        print('\n')
        print('c1: ' + self.color + ', c2: ' + other.color)
        print('1:(' + str(f1) + ', ' + str(b1) + '), 2:(' + str(f2) + ', ' + str(b2) + ')')
        print('\n')
        return self.getMinZ() < other.getMinZ()

    
    def isBoundingBoxOverlaping(self, value: object) -> bool:
        return ((self.getProjectedMaxY() <= value.getMinY()) or (self.getProjectedMinY >= value.getMaxY())) or ((self.getProjectedMaxX() <= value.getMinX()) or (self.getProjectedMinX >= value.getMaxX()))
        #return self.getMaxZ() == value.getMaxZ()
        #return sorted(self.points3D) == sorted(value.points3D)
    
    def __str__(self) -> str:
        return " " + self.color + " (" + str(self.getMinZ()) + ", " + str(self.getMaxZ()) + ") "# + str(self.normal)
    


def fixQuadOrder(quadList:list[Quad]) -> list[Quad]:
    
    pass






