import numpy as np
from math import tan, sin, cos, pi

TRANSLATION_AMMOUNT = 10
ROTATION_AMMOUNT = pi/36 

def perspectiveProjectionMatrix(w,h,fov,n,f):
    # w = width of the camera (screen)
    # h = height of the camera (screen)
    # fov = field of view (in radians)
    # n = distance to near plane
    # f = distance to far plane
    return np.array([[(1/((w/h) * tan(fov/2))), 0, 0, 0],
                     [0, (1/tan(fov/2)), 0, 0],
                     [0, 0, f/(f-n), ((-f) * n)/(f-n)],
                     [0, 0, 1, 0]])

def moveZup():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, -TRANSLATION_AMMOUNT],
                     [0, 0, 0, 1]])

def moveZdown():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, TRANSLATION_AMMOUNT],
                     [0, 0, 0, 1]])

def moveXup():
    return np.array([[1, 0, 0, -TRANSLATION_AMMOUNT],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def moveXdown():
    return np.array([[1, 0, 0, TRANSLATION_AMMOUNT],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def moveYup():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, -TRANSLATION_AMMOUNT],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def moveYdown():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, TRANSLATION_AMMOUNT],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def rotateYcw():
    return np.array([[cos(ROTATION_AMMOUNT), 0, sin(ROTATION_AMMOUNT), 0],
                     [0, 1, 0, 0],
                     [ -sin(ROTATION_AMMOUNT), 0, cos(ROTATION_AMMOUNT), 0],
                     [0, 0, 0, 1]])  

def rotateYccw():
    return np.array([[cos(-ROTATION_AMMOUNT), 0, sin(-ROTATION_AMMOUNT), 0],
                     [0, 1, 0, 0],
                     [-sin(-ROTATION_AMMOUNT), 0, cos(-ROTATION_AMMOUNT), 0],
                     [0, 0, 0, 1]]) 

def rotateXccw():
    return np.array([[1, 0, 0, 0],
                     [0, cos(ROTATION_AMMOUNT), -sin(ROTATION_AMMOUNT), 0],
                     [0, sin(ROTATION_AMMOUNT), cos(ROTATION_AMMOUNT), 0],
                     [0, 0, 0, 1]])  

def rotateXcw():
    return np.array([[1, 0, 0, 0],
                     [0, cos(-ROTATION_AMMOUNT), -sin(-ROTATION_AMMOUNT), 0],
                     [0, sin(-ROTATION_AMMOUNT), cos(-ROTATION_AMMOUNT), 0],
                     [0, 0, 0, 1]]) 

def rotateZcw():
    return np.array([[cos(ROTATION_AMMOUNT), -sin(ROTATION_AMMOUNT), 0, 0],
                     [sin(ROTATION_AMMOUNT), cos(ROTATION_AMMOUNT) , 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])  

def rotateZccw():
    return np.array([[cos(-ROTATION_AMMOUNT), -sin(-ROTATION_AMMOUNT), 0, 0],
                     [sin(-ROTATION_AMMOUNT), cos(-ROTATION_AMMOUNT) , 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])  