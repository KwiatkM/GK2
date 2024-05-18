from __future__ import annotations
import numpy as np
from tkinter import Canvas
from quad import Quad


class Cuboid:
    
    def __init__(self, x, y, z, width, height, deepth, color='red') -> None:
        #self.x = x
        #self.y = y
        #self.z = z
        #self.width = width
        #self.height = height
        #self.deepth = deepth
        self.ppn = [] #projected_points_normalized
        self.pp = [] #projected points in canvas coordinates
        self.points = []
        self.points.append(np.array([[x, y, z, 1]]).T)
        self.points.append(np.array([[x, y + height, z, 1]]).T)
        self.points.append(np.array([[x + width, y, z, 1]]).T)
        self.points.append(np.array([[x + width, y + height, z, 1]]).T)
        self.points.append(np.array([[x, y, z + deepth, 1]]).T)
        self.points.append(np.array([[x, y + height, z + deepth, 1]]).T)
        self.points.append(np.array([[x + width, y, z + deepth, 1]]).T)
        self.points.append(np.array([[x + width, y + height, z + deepth, 1]]).T)

        self.color = color


    
    def __str__(self) -> str:
        tmp = ""
        points = self.getPointsCoordinates()
        for point in points:
            tmp += str(point) + '\n'
        return tmp
    
    def project(self, projection:np.ndarray, canvas_height, canvas_width,):
        pp = [] # projected_points
        ppn = [] # projected_points_normalized
        for p in self.points:
            tmp = projection.dot(p)

            if tmp[3][0] == 0: 
                tmp = np.array([[float('inf'), float('inf'), float('inf'), 1]]).T
            else:
                tmp = tmp/(tmp[3][0])
        
            ppn.append(tmp)
            tmp[0][0] = (tmp[0][0] * canvas_width/2) + canvas_width/2
            tmp[1][0] = (-tmp[1][0] * canvas_height/2) + canvas_height/2
            pp.append(tmp)
        self.ppn = ppn
        self.pp = pp

    def getQuads(self) -> list[Quad]:
        color = self.color
        quads = []
        if self.checkZ(0,1,3,2):
            quads.append(Quad(np.array([(self.points[0].T).reshape(-1)[0:3], (self.points[1].T).reshape(-1)[0:3], (self.points[3].T).reshape(-1)[0:3], (self.points[2].T).reshape(-1)[0:3] ]),
                          np.array([self.pp[0], self.pp[1], self.pp[3], self.pp[2]]),
                          color=color))
        if self.checkZ(1,5,7,3):
            quads.append(Quad(np.array([(self.points[1].T).reshape(-1)[0:3], (self.points[5].T).reshape(-1)[0:3], (self.points[7].T).reshape(-1)[0:3], (self.points[3].T).reshape(-1)[0:3] ]),
                          np.array([self.pp[1], self.pp[5], self.pp[7], self.pp[3]]),
                          color=color))
        if self.checkZ(3,7,6,2):
            quads.append(Quad(np.array([(self.points[3].T).reshape(-1)[0:3], (self.points[7].T).reshape(-1)[0:3], (self.points[6].T).reshape(-1)[0:3], (self.points[2].T).reshape(-1)[0:3] ]),
                          np.array([self.pp[3], self.pp[7], self.pp[6], self.pp[2]]),
                          color=color))
        if self.checkZ(2,6,4,0):
            quads.append(Quad(np.array([(self.points[2].T).reshape(-1)[0:3], (self.points[6].T).reshape(-1)[0:3], (self.points[4].T).reshape(-1)[0:3], (self.points[0].T).reshape(-1)[0:3] ]),
                          np.array([self.pp[2], self.pp[6], self.pp[4], self.pp[0]]),
                          color=color))
        if self.checkZ(0,4,5,1):
            quads.append(Quad(np.array([(self.points[0].T).reshape(-1)[0:3], (self.points[4].T).reshape(-1)[0:3], (self.points[5].T).reshape(-1)[0:3], (self.points[1].T).reshape(-1)[0:3] ]),
                          np.array([self.pp[0], self.pp[4], self.pp[5], self.pp[1]]),
                          color=color))
        if self.checkZ(6,7,5,4):
            quads.append(Quad(np.array([(self.points[6].T).reshape(-1)[0:3], (self.points[7].T).reshape(-1)[0:3], (self.points[5].T).reshape(-1)[0:3], (self.points[4].T).reshape(-1)[0:3] ]),
                          np.array([self.pp[6], self.pp[7], self.pp[5], self.pp[4]]),
                          color=color))
        return quads
    
    def checkZ(self, z1, z2, z3, z4):
        if (self.ppn[z1][2][0] > 0 and self.ppn[z1][2][0] < 1) and\
            (self.ppn[z2][2][0] > 0 and self.ppn[z2][2][0] < 1) and\
            (self.ppn[z3][2][0] > 0 and self.ppn[z3][2][0] < 1) and\
            (self.ppn[z4][2][0] > 0 and self.ppn[z4][2][0] < 1):
            return True
        return False
        
        

    def drawBorders(self, canvas:Canvas, color='black', line_width=1):
        self.drawLine(self.pp[0][0][0], self.pp[0][1][0], self.pp[1][0][0], self.pp[1][1][0], self.ppn[0][2][0], self.ppn[1][2][0], canvas, color, line_width)
        self.drawLine(self.pp[0][0][0], self.pp[0][1][0], self.pp[2][0][0], self.pp[2][1][0], self.ppn[0][2][0], self.ppn[2][2][0], canvas, color, line_width)
        self.drawLine(self.pp[3][0][0], self.pp[3][1][0], self.pp[1][0][0], self.pp[1][1][0], self.ppn[3][2][0], self.ppn[1][2][0], canvas, color, line_width)
        self.drawLine(self.pp[3][0][0], self.pp[3][1][0], self.pp[2][0][0], self.pp[2][1][0], self.ppn[3][2][0], self.ppn[2][2][0], canvas, color, line_width)
        self.drawLine(self.pp[0][0][0], self.pp[0][1][0], self.pp[4][0][0], self.pp[4][1][0], self.ppn[0][2][0], self.ppn[4][2][0], canvas, color, line_width)
        self.drawLine(self.pp[1][0][0], self.pp[1][1][0], self.pp[5][0][0], self.pp[5][1][0], self.ppn[1][2][0], self.ppn[5][2][0], canvas, color, line_width)
        self.drawLine(self.pp[2][0][0], self.pp[2][1][0], self.pp[6][0][0], self.pp[6][1][0], self.ppn[2][2][0], self.ppn[6][2][0], canvas, color, line_width)
        self.drawLine(self.pp[3][0][0], self.pp[3][1][0], self.pp[7][0][0], self.pp[7][1][0], self.ppn[3][2][0], self.ppn[7][2][0], canvas, color, line_width)
        self.drawLine(self.pp[4][0][0], self.pp[4][1][0], self.pp[5][0][0], self.pp[5][1][0], self.ppn[4][2][0], self.ppn[5][2][0], canvas, color, line_width)
        self.drawLine(self.pp[4][0][0], self.pp[4][1][0], self.pp[6][0][0], self.pp[6][1][0], self.ppn[4][2][0], self.ppn[6][2][0], canvas, color, line_width)
        self.drawLine(self.pp[7][0][0], self.pp[7][1][0], self.pp[5][0][0], self.pp[5][1][0], self.ppn[7][2][0], self.ppn[5][2][0], canvas, color, line_width)
        self.drawLine(self.pp[7][0][0], self.pp[7][1][0], self.pp[6][0][0], self.pp[6][1][0], self.ppn[7][2][0], self.ppn[6][2][0], canvas, color, line_width)

        
    def drawLine(self, x1, y1, x2, y2, zn1, zn2, canvas:Canvas, color='black', line_width=1):
        if (zn1 > 0 and zn1 < 1) and (zn2 > 0 and zn2 < 1):
            canvas.create_line(x1, y1, x2, y2, fill=color, width=line_width)
   

    def applyTransformation(self, transformation:np.ndarray):
        for i, point in enumerate(self.points):
            tmp = transformation.dot(point)
            tmp = tmp/(tmp[3][0])
            self.points[i] = tmp
    


        