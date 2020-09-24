import keyboard as key
from tkinter import *
import time
import numpy as np
import random

import shapes as sh
import parameters as par
import cube_row as cube

# Set parameters
index_width = par.index_width
index_height = par.index_height

# Initialize canvas
tk = Tk()
canvas = Canvas(tk, width=par.screen_width, height=par.screen_height, bg="white")
canvas.pack()

# Set parameters
fps=1

frame_rate = par.frame_rate
xstep = par.xstep
ystep = par.ystep

# Load shapes
shape_list = par.shape_list
shape = "Z"

# Set parameters
score = 0
array = np.empty([index_width,index_height], dtype = object) # Initialize cube array.
orientation = 0 # orientation of Tetris block.
begin_origin = [round(index_width/2),0] # Initial coordinates of Tetris block.
origin = begin_origin # coordinates of Tetris block.
v1 = v2 = v3 = v4 = np.array([[0],[0]]) # Vectors that specify the location of the Tetris block cubes relative to the origin.
while True:

    # Start timer
    start_time = time.time()

    # Move Tetris block left when there is no left boundary.
    touch_left_border = sh.get_touch_left_border(origin, v1, v2, v3, v4)
    if key.is_pressed("left") and not touch_left_border:
        origin[0] -= 1

    # Move Tetris block right when there is no right boundary.
    touch_right_border = sh.get_touch_right_border(origin, v1, v2, v3, v4)
    if key.is_pressed("right") and not touch_right_border:
        origin[0] += 1

    # Reset game
    if key.is_pressed("r"):
        score = 0
        array = np.empty([index_width,index_height], dtype = object)
        orientation = 0
        begin_origin = [round(index_width/2),0]
        origin = begin_origin
        v1 = v2 = v3 = v4 = np.array([[0],[0]])

    # Check if boundary is crossed when rotating the Tetris block.
    touch_rotation_left_border = sh.get_touch_rotation_left_border(origin, v1, v2, v3, v4)
    touch_rotation_right_border = sh.get_touch_rotation_right_border(origin, v1, v2, v3, v4)

    # Rotate Tetris block
    if key.is_pressed("enter") and not touch_rotation_left_border and not touch_rotation_right_border:
        orientation = (orientation + 1) % 4

    # Quiz game
    if key.is_pressed("esc"):
        break

    # Move Tetris block down.
    previous_origin = origin[1]
    origin[1] += 1

    # Delete row when full.
    array = cube.delete_row(array)

    # Reset canvas
    canvas.delete("all")

    # Get positions of cubes that make up the Tetris block.
    v1, v2, v3, v4, color = sh.get_shape(origin[0],origin[1],orientation,canvas,shape)

    # See if the Tetris block is going to collide with other cubes. When true merge the Tetris block with the cube array.
    array, collision = cube.cube_array(origin, v1, v2, v3, v4, color, canvas, array)

    # Increment score when Tetris block merges cube array. And generate a new Tetris block.
    if collision or origin[1] >= index_height:
        begin_origin = [round(index_width/2),0]
        origin = begin_origin
        score +=100
        shape = random.choice(shape_list)

    # When the cube array is full the game is reset.
    if collision and previous_origin == origin[1]:
        score = 0
        array = np.empty([index_width,index_height], dtype = object)
        orientation = 0
        begin_origin = [round(index_width/2),0]
        origin = begin_origin
        v1 = v2 = v3 = v4 = np.array([[0],[0]])

    # Put score and frame rate on canvas.
    canvas.create_text(100,30,fill="blue",font="Times 20 italic bold",
                        text="score:" + str(score))
    canvas.create_text(100,10,fill="blue",font="Times 20 italic bold",
                        text="fps:" + str(fps))

    # Put canvas on screen.
    canvas.update()
    time.sleep(max(abs(1/frame_rate-(time.time() - start_time)),1/10000000)) # Sleep in order to control frame rate.

    #Calculate frame rate.
    fps =round(1.0 / (time.time() - start_time),2)
    #print("FPS: ", fps)
