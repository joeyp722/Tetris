import numpy as np
from tkinter import *

import parameters as par
import shapes as sh

# Initialize parameters.
xstep = par.xstep
ystep = par.ystep
index_width = par.index_width
index_height = par.index_height

def cube_array(origin, v1, v2, v3, v4, color, canvas, array):

    block_array = np.empty([index_width,index_height], dtype = object)

    # Put Tetris block in the block array.
    if (origin[1]+v1[1,0]) < index_height and (origin[1]+v2[1,0]) < index_height and (origin[1]+v3[1,0]) < index_height and (origin[1]+v4[1,0]) < index_height:
        block_array[origin[0]+v1[0,0],origin[1]+v1[1,0]]=color
        block_array[origin[0]+v2[0,0],origin[1]+v2[1,0]]=color
        block_array[origin[0]+v3[0,0],origin[1]+v3[1,0]]=color
        block_array[origin[0]+v4[0,0],origin[1]+v4[1,0]]=color

    # Draw all the cubes in the cube array on the canvas.
    for i in range(index_width):
        for j in range(index_height):
            if array[i,j] != None:
                color = array[i,j]
                sh.square(i*xstep,j*ystep,color,canvas)

    # If the Tetris block collides with other cubes, then add the block array to the cube array.
    collision = get_collision(array,block_array)
    if collision:
        array = append_array(array,block_array)

    return array, collision;

def get_collision(array, block_array):
    collision = False
    shift_array = np.empty([index_width,index_height], dtype = object)

    # Create shift array, where the cube array is moved down one position.
    for i in range(index_width):
        for j in range(index_height-1):
            shift_array[i,j+1] = block_array[i,j]

    for i in range(index_width):
        for j in range(index_height):
            if array[i,j] != None and shift_array[i,j] != None:
                collision = True
                break

    for i in range(index_width):
        if block_array[i,index_height-1] != None:
            collision = True
            break

    return collision;

# Merge Tetris block with the cube array.
def append_array(array,block_array):
    for i in range(index_width):
        for j in range(index_height):
            if block_array[i,j] != None:
                    array[i,j] = block_array[i,j]
    return array;

def delete_row(array):

    # Check for every row.
    for i in range(index_height):
        counter = 0

        # Count the number of cubes in row.
        for j in range(index_width):
            if array[j,i] != None:
                counter += 1

        # If a row is full then delete the row.
        if counter >=index_width:
            for j in range(index_width):
                array[j,i] = array[j,i-1]

    return array
