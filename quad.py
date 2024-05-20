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
    
    def __init__(self, borderPoints:np.ndarray,  color=(1,0,0), div0 = 0, div1 = 0) -> None:
        self.borderPoints = borderPoints
        self.div0 = div0
        self.div1 = div1

        #Ax + By + Cz + D = 0
        self.normal = np.cross((borderPoints[1] - borderPoints[0])[0:3],(borderPoints[2] - borderPoints[0])[0:3])
        self.d = -np.dot(borderPoints[0][0:3], self.normal)
        normal_len = np.sqrt( np.dot(self.normal, self.normal))
        self.normal = self.normal/normal_len
        self.d = self.d/normal_len

        self.facingCamera = False
        if self.d > 0:
            self.facingCamera = True
        self.isZinRange = True

        self.color = self.darkenColor(color)
        

    def createPoitMatrix(self):
        v0to1 = self.borderPoints[1] - self.borderPoints[0]
        v1to2 = self.borderPoints[2] - self.borderPoints[1]
        nOf0 = self.div0 + 1
        nOf1 = self.div1 + 1
        step0 = v0to1/nOf0
        step1 = v1to2/nOf1
        pointMatrix = np.zeros((nOf1+1, nOf0+1, 4))

        for i in range(nOf1+1):
            for j in range(nOf0+1):
                pointMatrix[i][j] = self.borderPoints[0] + (i * step1) + (j * step0)

        self.pointMatrix = pointMatrix


    def project(self, projection:np.ndarray, canvas_height, canvas_width):
        self
        p = np.zeros(self.pointMatrix.shape)
        for i in range(self.pointMatrix.shape[0]):
            for j in range(self.pointMatrix.shape[1]):
                p[i][j] = projection.dot(self.pointMatrix[i][j])
                if p[i][j][3] == 0: p[i][j] = np.array([float('inf'), float('inf'), float('inf'), 1])
                p[i][j] = p[i][j] / p[i][j][3]
                p[i][j][0] = (p[i][j][0] * canvas_width/2) + canvas_width/2
                p[i][j][1] = (-p[i][j][1] * canvas_height/2) + canvas_height/2
                #print(p[i][j])
                if p[i][j][2] < 0 or p[i][j][2] > 1.0: self.isZinRange = False
            #print("------------------")
        self.projectedPoints = p
    

    def getQuadlets(self) -> list[Quadlet]:
        quadlets = []
        for i in range(self.projectedPoints.shape[0]-1):
            for j in range(self.projectedPoints.shape[1]-1):
                quadlets.append(Quadlet([self.projectedPoints[i][j][0:2], self.projectedPoints[i][j+1][0:2], self.projectedPoints[i+1][j+1][0:2], self.projectedPoints[i+1][j][0:2]],
                                        (self.pointMatrix[i][j][2] + self.pointMatrix[i+1][j+1][2])/2,
                                         color=self.color ))
        return quadlets
    
    def darkenColor(self, rgbTuple):
        hsv = colorsys.rgb_to_hsv(rgbTuple[0], rgbTuple[1], rgbTuple[2])
        cos = -np.dot(self.normal, np.array([0,0,1]))
        if cos<=0.0: cos = 0.0
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]*((cos * 0.2) + 0.8))
        return '#%02x%02x%02x' % (round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255))
    
    def copyColor(self, rgbTuple):
        return '#%02x%02x%02x' % (round(rgbTuple[0] * 255), round(rgbTuple[1] * 255), round(rgbTuple[2] * 255))

    
    
class Quadlet():
    
    def __init__(self, projectedPoints:np.ndarray, z, color:str) -> None:
        self.projectedPoints = projectedPoints
        self.z = z
        self.color = color

    def draw(self, canvas:Canvas):
        canvas.create_polygon(self.projectedPoints[0][0], self.projectedPoints[0][1],
                              self.projectedPoints[1][0], self.projectedPoints[1][1],
                              self.projectedPoints[2][0], self.projectedPoints[2][1],
                              self.projectedPoints[3][0], self.projectedPoints[3][1],
                              fill=self.color)
        canvas.create_line(self.projectedPoints[0][0], self.projectedPoints[0][1], self.projectedPoints[1][0], self.projectedPoints[1][1], fill='black', width=1)
        canvas.create_line(self.projectedPoints[1][0], self.projectedPoints[1][1], self.projectedPoints[2][0], self.projectedPoints[2][1], fill='black', width=1)
        canvas.create_line(self.projectedPoints[2][0], self.projectedPoints[2][1], self.projectedPoints[3][0], self.projectedPoints[3][1], fill='black', width=1)
        canvas.create_line(self.projectedPoints[3][0], self.projectedPoints[3][1], self.projectedPoints[0][0], self.projectedPoints[0][1], fill='black', width=1)







