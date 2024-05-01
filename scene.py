from cuboid import Cuboid
from tkinter import Canvas
from math import pi
import transformations as t
import numpy as np

class Scene():

    FOV_INCREASE_AMMOUNT = pi/36
    
    def __init__(self, cuboids: list[Cuboid], canvas: Canvas, canvas_height:int, canvas_width:int) -> None:
        self.cuboids = cuboids
        self.canvas = canvas
        
        self.fov = pi/2
        self.cam_height = canvas_height
        self.cam_width = canvas_width
        self.near_plane_distance = 1
        self.far_plane_distance = 1000
        
        self.updateProjectionMatrix()
        
        
    def updateProjectionMatrix(self):
        self.projection_matrix = t.perspectiveProjectionMatrix(self.cam_width,
                                                             self.cam_height,
                                                             self.fov,
                                                             self.near_plane_distance,
                                                             self.far_plane_distance)
        
        
    def render(self):
        for c in self.cuboids:
            c.projectAndDraw(self.projection_matrix, self.canvas, self.cam_height, self.cam_width)
        self.canvas.create_text(35,10,text='fov: ' + str(round((self.fov * (360/(2*pi))), 2)))
    
    def refresh(self):
        self.canvas.delete("all")
        self.render()

    def transform(self, transformation:np.ndarray):
        for cuboid in self.cuboids:
            cuboid.applyTransformation(transformation)
    

    def moveBack(self):
        self.transform(t.moveZup())

    def moveFront(self):
        self.transform(t.moveZdown())

    def moveUp(self):
        self.transform(t.moveYup())

    def moveDown(self):
        self.transform(t.moveYdown())

    def moveRight(self):
        self.transform(t.moveXup())

    def moveLeft(self):
        self.transform(t.moveXdown())
    
    def rotateYcw(self):
        self.transform(t.rotateYcw())

    def rotateYccw(self):
        self.transform(t.rotateYccw())

    def rotateXcw(self):
        self.transform(t.rotateXcw())

    def rotateXccw(self):
        self.transform(t.rotateXccw())

    def rotateZcw(self):
        self.transform(t.rotateZcw())

    def rotateZccw(self):
        self.transform(t.rotateZccw())
    
    def fovDown(self):
        if self.fov - self.FOV_INCREASE_AMMOUNT < 0:
            self.fov = 0
        else:
            self.fov -= self.FOV_INCREASE_AMMOUNT
        self.updateProjectionMatrix()

    def fovUp(self):
        self.fov += self.FOV_INCREASE_AMMOUNT
        self.updateProjectionMatrix()
    
    
        