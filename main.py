import tkinter as tk
import cuboid as c
from scene import Scene

WIDTH = 800
HEIGHT = 800

window  = tk.Tk()
window.geometry("" + str(WIDTH) + "x" + str(HEIGHT))

canvas = tk.Canvas(window, bg='grey75', width=WIDTH, height=HEIGHT)
canvas.pack()

c1 = c.Cuboid(10, -20, 50, 20,20,20)
c2 = c.Cuboid(-20, -20, 40, 20,30,40)
c3 = c.Cuboid(10, -20, 80, 50,40,20)
c4 = c.Cuboid(-20, -20, 100, 20,20,20)

scene = Scene([c1,c2,c3,c4], canvas, HEIGHT, WIDTH)
scene.render()

def mv_up(event):
    scene.moveUp()
    scene.refresh()

def mv_down(event):
    scene.moveDown()
    scene.refresh()

def mv_left(event):
    scene.moveLeft()
    scene.refresh()

def mv_right(event):
    scene.moveRight()
    scene.refresh()

def mv_front(event):
    scene.moveFront()
    scene.refresh()

def mv_back(event):
    scene.moveBack()
    scene.refresh()

#rotate Y clockwise
def rotYcw(event): 
    scene.rotateYcw()
    scene.refresh()

#rotate Y counterclockwise
def rotYccw(event): 
    scene.rotateYccw()
    scene.refresh()

#rotate X clockwise
def rotXcw(event): 
    scene.rotateXcw()
    scene.refresh()

#rotate X counterclockwise
def rotXccw(event): 
    scene.rotateXccw()
    scene.refresh()

#rotate Z clockwise
def rotZcw(event): 
    scene.rotateZcw()
    scene.refresh()

#rotate Z counterclockwise
def rotZccw(event): 
    scene.rotateZccw()
    scene.refresh()

def fovUp(event): 
    scene.fovUp()
    scene.refresh()

def fovDown(event):
    scene.fovDown()
    scene.refresh()

window.bind('<Up>', mv_up)
window.bind('<Down>', mv_down)
window.bind('<Left>', mv_left)
window.bind('<Right>', mv_right)
window.bind('z', mv_front)
window.bind('x', mv_back)
window.bind('a', rotYcw)
window.bind('d', rotYccw)
window.bind('w', rotXcw)
window.bind('s', rotXccw)
window.bind('q', rotZcw)
window.bind('e', rotZccw)
window.bind('r', fovUp)
window.bind('f', fovDown)


window.mainloop()
