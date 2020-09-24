import parameters as par
import numpy as np
from tkinter import *

index_width = par.index_width
index_height = par.index_height

xstep = par.xstep
ystep = par.ystep

def square(x,y,color,canvas):
    canvas.create_rectangle(x, y, x+xstep, y+ystep, fill=color) # Draw Tetris cube on canvas.

def Ishape(x,y,orientation,canvas):

    # Define I Tetris block.
    color = "green"
    v1 = np.array([[-1],[0]])
    v2 = np.array([[0],[0]])
    v3 = np.array([[1],[0]])
    v4 = np.array([[2],[0]])

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])
    for i in range(orientation):
        v1 = np.dot(rotation,v1)
        v2 = np.dot(rotation,v2)
        v3 = np.dot(rotation,v3)
        v4 = np.dot(rotation,v4)

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def Jshape(x,y,orientation,canvas):

    # Define J Tetris block.
    color = "blue"
    v1 = np.array([[-1],[-1]])
    v2 = np.array([[-1],[0]])
    v3 = np.array([[0],[0]])
    v4 = np.array([[1],[0]])

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])
    for i in range(orientation):
        v1 = np.dot(rotation,v1)
        v2 = np.dot(rotation,v2)
        v3 = np.dot(rotation,v3)
        v4 = np.dot(rotation,v4)

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def Lshape(x,y,orientation,canvas):

    # Define L Tetris block.
    color = "orange"
    v1 = np.array([[-1],[0]])
    v2 = np.array([[0],[0]])
    v3 = np.array([[1],[0]])
    v4 = np.array([[1],[1]])

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])
    for i in range(orientation):
        v1 = np.dot(rotation,v1)
        v2 = np.dot(rotation,v2)
        v3 = np.dot(rotation,v3)
        v4 = np.dot(rotation,v4)

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def Oshape(x,y,orientation,canvas):

    # Define O Tetris block.
    color = "yellow"
    v1 = np.array([[0],[0]])
    v2 = np.array([[1],[0]])
    v3 = np.array([[0],[1]])
    v4 = np.array([[1],[1]])

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def Sshape(x,y,orientation,canvas):

    # Define S Tetris block.
    color = "pink"
    v1 = np.array([[-1],[0]])
    v2 = np.array([[0],[0]])
    v3 = np.array([[0],[1]])
    v4 = np.array([[1],[1]])

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])
    for i in range(orientation):
        v1 = np.dot(rotation,v1)
        v2 = np.dot(rotation,v2)
        v3 = np.dot(rotation,v3)
        v4 = np.dot(rotation,v4)

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def Tshape(x,y,orientation,canvas):

    # Define T Tetris block.
    color = "purple"
    v1 = np.array([[-1],[0]])
    v2 = np.array([[0],[0]])
    v3 = np.array([[0],[1]])
    v4 = np.array([[1],[0]])

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])
    for i in range(orientation):
        v1 = np.dot(rotation,v1)
        v2 = np.dot(rotation,v2)
        v3 = np.dot(rotation,v3)
        v4 = np.dot(rotation,v4)

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def Zshape(x,y,orientation,canvas):

    # Define Z Tetris block.
    color = "red"
    v1 = np.array([[-1],[1]])
    v2 = np.array([[0],[1]])
    v3 = np.array([[0],[0]])
    v4 = np.array([[1],[0]])

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])
    for i in range(orientation):
        v1 = np.dot(rotation,v1)
        v2 = np.dot(rotation,v2)
        v3 = np.dot(rotation,v3)
        v4 = np.dot(rotation,v4)

    # Draw Tetris block on canvas.
    square((x+v1[0,0])*xstep,(y+v1[1,0])*ystep,color,canvas)
    square((x+v2[0,0])*xstep,(y+v2[1,0])*ystep,color,canvas)
    square((x+v3[0,0])*xstep,(y+v3[1,0])*ystep,color,canvas)
    square((x+v4[0,0])*xstep,(y+v4[1,0])*ystep,color,canvas)

    return v1, v2, v3, v4, color;

def get_touch_left_border(origin, v1, v2, v3, v4):

    touch_left_border = False

    # Check if Tetris block touches left border.
    if (origin[0]+v1[0,0]) <= 0 or (origin[0]+v3[0,0]) <= 0 or (origin[0]+v3[0,0]) <= 0 or (origin[0]+v4[0,0]) <= 0:
         touch_left_border = True

    return touch_left_border

def get_touch_right_border(origin, v1, v2, v3, v4):

    touch_right_border = False

    # Check if Tetris block touches right border.
    if (origin[0]+v1[0,0]) >= index_width-1 or (origin[0]+v3[0,0]) >= index_width-1 or (origin[0]+v3[0,0]) >= index_width-1 or (origin[0]+v4[0,0]) >= index_width-1:
         touch_right_border = True

    return touch_right_border

def get_touch_rotation_left_border(origin, v1, v2, v3, v4):

    touch_rotation_left_border = False

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])

    v1 = np.dot(rotation,v1)
    v2 = np.dot(rotation,v2)
    v3 = np.dot(rotation,v3)
    v4 = np.dot(rotation,v4)

    # Check if the rotation causes a collision with the left boundary.
    if (origin[0]+v1[0,0]) <= 0 or (origin[0]+v3[0,0]) <= 0 or (origin[0]+v3[0,0]) <= 0 or (origin[0]+v4[0,0]) <= 0:
         touch_rotation_left_border = True

    return touch_rotation_left_border

def get_touch_rotation_right_border(origin, v1, v2, v3, v4):

    touch_rotation_right_border = False

    # Rotate Tetris block.
    rotation = np.array([[0, -1],[1,0]])

    v1 = np.dot(rotation,v1)
    v2 = np.dot(rotation,v2)
    v3 = np.dot(rotation,v3)
    v4 = np.dot(rotation,v4)

    # Check if the rotation causes a collision with the right boundary.
    if (origin[0]+v1[0,0]) >= index_width-1 or (origin[0]+v3[0,0]) >= index_width-1 or (origin[0]+v3[0,0]) >= index_width-1 or (origin[0]+v4[0,0]) >= index_width-1:
         touch_rotation_right_border = True

    return touch_rotation_right_border

def get_shape(origin_x,origin_y,orientation,canvas,shape):

    # Select shape
    if shape == "I":
        v1, v2, v3, v4, color = Ishape(origin_x,origin_y,orientation,canvas)
    elif shape == "J":
        v1, v2, v3, v4, color = Jshape(origin_x,origin_y,orientation,canvas)
    elif shape == "L":
        v1, v2, v3, v4, color = Lshape(origin_x,origin_y,orientation,canvas)
    elif shape == "O":
        v1, v2, v3, v4, color = Oshape(origin_x,origin_y,orientation,canvas)
    elif shape == "S":
        v1, v2, v3, v4, color = Sshape(origin_x,origin_y,orientation,canvas)
    elif shape == "T":
        v1, v2, v3, v4, color = Tshape(origin_x,origin_y,orientation,canvas)
    elif shape == "Z":
        v1, v2, v3, v4, color = Zshape(origin_x,origin_y,orientation,canvas)
    else:
        v1, v2, v3, v4, color = Zshape(origin_x,origin_y,orientation,canvas)

    return v1, v2, v3, v4, color
