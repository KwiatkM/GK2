from functools import total_ordering
import numpy as np
from tkinter import Canvas
import colorsys


class Quadlet():
    
    def __init__(z:float, pp:np.ndarray, color:str ) -> None:
        pass

    def draw(canvas:Canvas):
        pass


class Quad:
    
    def __init__(self, points3D:np.ndarray, pp:np.ndarray,  color=(1,0,0)) -> None:
        # points3D = 4 points (in order) in camera coordinates that form a quad
        # for each point: 
        #   first element = x
        #   second element = y
        #   third element = z
        self.points3D = points3D
        self.pp = pp
        
        #Ax + By + Cz + D = 0
        self.normal = np.cross(points3D[1] - points3D[0],points3D[2] - points3D[0])
        self.d = -np.dot(points3D[0], self.normal)
        normal_len = np.sqrt( self.normal[0]*self.normal[0] + self.normal[1]*self.normal[1] + self.normal[2]*self.normal[2])
        self.normal = self.normal/normal_len
        self.d = self.d/normal_len

        self.facingCamera = False
        if self.d > 0:
            self.facingCamera = True
        self.maxz = self.getMaxZ()

        self.color = darkenColor(color, self.normal)

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

    
    
    def draw(self, canvas:Canvas):
        canvas.create_polygon(self.pp[0][0][0], self.pp[0][1][0],
                              self.pp[1][0][0], self.pp[1][1][0],
                              self.pp[2][0][0], self.pp[2][1][0],
                              self.pp[3][0][0], self.pp[3][1][0],
                              fill=self.color)
        #canvas.create_line(self.pp[0][0][0], self.pp[0][1][0], self.pp[1][0][0], self.pp[1][1][0], fill='black', width=1)
        #canvas.create_line(self.pp[1][0][0], self.pp[1][1][0], self.pp[2][0][0], self.pp[2][1][0], fill='black', width=1)
        #canvas.create_line(self.pp[2][0][0], self.pp[2][1][0], self.pp[3][0][0], self.pp[3][1][0], fill='black', width=1)
        #canvas.create_line(self.pp[3][0][0], self.pp[3][1][0], self.pp[0][0][0], self.pp[0][1][0], fill='black', width=1)
        #canvas.create_oval(self.pp[0][0][0], self.pp[0][1][0], self.pp[0][0][0]+10, self.pp[0][1][0]+10, fill='firebrick4')
        #canvas.create_oval(self.pp[1][0][0], self.pp[1][1][0], self.pp[1][0][0]+10, self.pp[1][1][0]+10, fill='gold')
        #canvas.create_oval(self.pp[2][0][0], self.pp[2][1][0], self.pp[2][0][0]+10, self.pp[2][1][0]+10, fill='green2')
    
    #def __lt__(self,other) -> bool:
    #    return self.isFurtherThan(other)

    def divideQuad(self, cutLen:int) -> list[Quadlet]:
        len0to1 = np.sqrt(np.dot(self.points3D[0], self.points3D[1]))
        len1to2 = np.sqrt(np.dot(self.points3D[1], self.points3D[2]))
        divCount0to1 = np.floor(len0to1 / cutLen)
        divCount1to2 = np.floor(len1to2 / cutLen)
        if divCount0to1 == 0: divCount0to1 = 1
        if divCount1to2 == 0: divCount1to2 = 1
        step0to1 = len0to1 / divCount0to1
        step1to2 = len1to2 / divCount1to2
        
        quadlets = []
        

    
        
    
    def __str__(self) -> str:
        return " " + self.color + ", normal=" + str(self.normal) + " " + str(self.d) + ", X range: (" + str(self.getProjectedMinX()) + ', ' + str(self.getProjectedMaxX()) + '), Y range: (' + str(self.getProjectedMinY()) + ', ' + str(self.getProjectedMaxY()) + ')'
    
    
    #" (" + str(self.getMinZ()) + ", " + str(self.getMaxZ()) + ") "# + str(self.normal)
    


def darkenColor(rgbTuple, normalVector):
    hsv = colorsys.rgb_to_hsv(rgbTuple[0], rgbTuple[1], rgbTuple[2])
    cos = -np.dot(normalVector, np.array([0,0,1]))
    if cos<=0.3: cos = 0.3
    rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]*cos)
    return '#%02x%02x%02x' % (round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255))






