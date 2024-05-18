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
        self.normal = np.cross(points3D[1] - points3D[0],points3D[2] - points3D[0])
        self.d = np.dot(points3D[0], self.normal)
        self.facingCamera = False
        if self.d < 0:
            self.facingCamera = True
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
        #canvas.create_oval(self.pp[0][0][0], self.pp[0][1][0], self.pp[0][0][0]+10, self.pp[0][1][0]+10, fill='firebrick4')
        #canvas.create_oval(self.pp[1][0][0], self.pp[1][1][0], self.pp[1][0][0]+10, self.pp[1][1][0]+10, fill='gold')
        #canvas.create_oval(self.pp[2][0][0], self.pp[2][1][0], self.pp[2][0][0]+10, self.pp[2][1][0]+10, fill='green2')
    
    #def __lt__(self,other) -> bool:
    #    return self.isFurtherThan(other)



    def isFurtherThan(self,other):
        #if not self.isProjectionOverlaping(other): return False
       
        if self.getMaxZ() <= other.getMinZ(): return False
        if self.getMinZ() >= other.getMaxZ(): return True

        

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


        return self.getMinZ() > other.getMinZ()

    def isProjectionOverlaping(self,other):
        # check if projections overlap
        if not self.isBoundingBoxOverlaping(other): return False
        if self.isContainedIn(other): return True
        if other.isContainedIn(self): return True
        if not self.isQuadOverlaping(other) : return False 
        return True

    def isBoundingBoxOverlaping(self, value: "Quad") -> bool:
        #return not (((self.getProjectedMaxY() <= value.getProjectedMinY()) or (self.getProjectedMinY() >= value.getProjectedMaxY()))) and (((self.getProjectedMaxX() <= value.getProjectedMinX()) or (self.getProjectedMinX() >= value.getProjectedMaxX())))
        return (self.getProjectedMaxX() >= value.getProjectedMinX() and value.getProjectedMaxX() >= self.getProjectedMinX()) and (self.getProjectedMaxY() >= value.getProjectedMinY() and value.getProjectedMaxY() >= self.getProjectedMinY())

    def isQuadOverlaping(self, other: "Quad") -> bool:
        for A, B in [(self.pp[0], self.pp[1]), (self.pp[1], self.pp[2]), (self.pp[2], self.pp[3]), (self.pp[3], self.pp[0])]:
            tmp = 0.00001
            if not(B[0][0] - A[0][0] == 0): tmp = B[0][0] - A[0][0]
            m1 = (B[1][0] - A[1][0]) / tmp
            b1 = A[1][0] - m1 * A[0][0]
            for C, D in [(other.pp[0], other.pp[1]), (other.pp[1], other.pp[2]), (other.pp[2], other.pp[3]), (other.pp[3], other.pp[0])]:
                tmp = 0.00001
                if not(D[0][0] - C[0][0] == 0): tmp= D[0][0] - C[0][0]
                m2 = (D[1][0] - C[1][0]) / tmp
                b2 = C[1][0] - m2 * C[0][0]

                if abs(m1 - m2) < 10e-4: continue
                tmp = 0.00001
                if not(m1-m2 == 0): tmp = m1-m2
                x_intersect=((b2-b1)/tmp)
                y_intersect=(m1*x_intersect)+b1

                if (x_intersect < A[0][0] and x_intersect > B[0][0]) or (x_intersect > A[0][0] and x_intersect < B[0][0]) and\
                (y_intersect < A[1][0] and y_intersect > B[1][0]) or (y_intersect > A[1][0] and y_intersect < B[1][0]) and\
                (x_intersect < C[0][0] and x_intersect > D[0][0]) or (x_intersect > C[0][0] and x_intersect < D[0][0]) and\
                (y_intersect < C[1][0] and y_intersect > D[1][0]) or (y_intersect > C[1][0] and y_intersect < D[1][0]):
                    return True
    
    def isContainedIn(self, other: "Quad") -> bool:
        return (self.getProjectedMinX() >= other.getProjectedMinX() and self.getProjectedMaxX() <= other.getProjectedMaxX()) and (self.getProjectedMinY() >= other.getProjectedMinY() and self.getProjectedMaxY() <= other.getProjectedMaxY())



        
    
    def __str__(self) -> str:
        return " " + self.color + ", normal=" + str(self.normal) + " " + str(self.d) + ", X range: (" + str(self.getProjectedMinX()) + ', ' + str(self.getProjectedMaxX()) + '), Y range: (' + str(self.getProjectedMinY()) + ', ' + str(self.getProjectedMaxY()) + ')'
    
    
    #" (" + str(self.getMinZ()) + ", " + str(self.getMaxZ()) + ") "# + str(self.normal)
    


def fixQuadOrder(quadList:list[Quad]) -> list[Quad]:
    
    pass






