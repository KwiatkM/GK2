import tkinter as tk
import cuboid as c
from scene import Scene
import transformations as t

WIDTH = 800
HEIGHT = 800

window  = tk.Tk()
window.geometry("" + str(WIDTH) + "x" + str(HEIGHT))

canvas = tk.Canvas(window, bg='grey75', width=WIDTH, height=HEIGHT)
canvas.pack()

c1 = c.Cuboid(15, -30, 45, 20,20,20, (1,0,0))
c2 = c.Cuboid(-30, -20, 40, 20,30,40, (0.0705, 0.7804, 0.0078))
c3 = c.Cuboid(10, -25, 80, 50,40,20, (0.0820, 0.875, 0.9179))
c4 = c.Cuboid(-35, -30, 100, 20,20,20, (0.9179, 0.75, 0.0820))

c5 = c.Cuboid(-60, -100, 45, 120,10,120, (0.894, 0.102, 0.11), divX=6, divY=2, divZ=6)
c5.applyTransformation(t.rotateXcw())
c5.applyTransformation(t.rotateXcw())
c5.applyTransformation(t.rotateXcw())
c5.applyTransformation(t.rotateXcw())
c5.applyTransformation(t.rotateXcw())
c5.applyTransformation(t.rotateXcw())
c5.applyTransformation(t.rotateXcw())

c6 = c.Cuboid(-60, -80, 60, 120,10,120, (0.216, 0.494, 0.722), divX=6, divY=2, divZ=6)
c6.applyTransformation(t.rotateXcw())
c6.applyTransformation(t.rotateXcw())
c6.applyTransformation(t.rotateXcw())
c6.applyTransformation(t.rotateXcw())
c6.applyTransformation(t.rotateXcw())
c6.applyTransformation(t.rotateXcw())
c6.applyTransformation(t.rotateXcw())


#scene = Scene([c1, c2, c3, c4], canvas, HEIGHT, WIDTH)
scene = Scene([c5, c6], canvas, HEIGHT, WIDTH)
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

def debugDraw(event):
    scene.debugDraw()

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
window.bind('<Escape>', debugDraw)


window.mainloop()
