# -*- coding: utf-8 -*- #
"""
Author: K Srirama Srikar
Date: 13.08.2024
Course: DS2030 Data Structures and Algorithms for Data Science
Lab: Lab 1 (In-person)
"""

import numpy as np
from PIL import Image

# import functions of numpy and pillow

with open('/input.txt', 'r') as file:
    # reading the file names
    lines = file.readlines()
    inps = []
    # to store the values and operations given in the .txt file
    for line in lines:
	if line.strip() != "":
	    # just to make sure there aren't any blank lines
	    line_list = []
	    # list of to store the words in the line
	    line_list = line.split()
      	    inps.append({'image_path': "/"+line_list[0],'operation' : line_list[1], 'params' : line_list[2:]})
      	    # appending a dictionary to the inputs list...


# image_file = '/image1.jpeg'
# image = np.array(Image.open(image_file))


def translate_image(image, x_offset, y_offset):
    h = len(image)
    w = len(image[0])
    cl = len(image[0][0])
    # stornig the height, width and the no. of colours in the image in h, w, cl respectively
    new_arr = np.zeros((h,w,cl), dtype=np.uint8)
    # creating an array of zeros of the type unsigned 8 bit integer 
    for i in range(0,h-x_offset):
        for j in range(0,w-y_offset):
        # the off set algorithm
            new_arr[i+x_offset][j+y_offset][0] = image[i][j][0]
            new_arr[i+x_offset][j+y_offset][1] = image[i][j][1]
            new_arr[i+x_offset][j+y_offset][2] = image[i][j][2]
    return new_arr

def flip_image(image, axis):
    h, w, cl = image.shape
    new_arr = np.zeros((h,w,cl), dtype=np.uint8)
    if axis==0:
    	# if axis = 0 it flips the image with respect to x-axis else y-axis
        for i in range(h-1,-1,-1):
            for j in range(0,w):
                new_arr[i][j] = image[h-1-i][j]
    else:
       for i in range(0,h):
           for j in range(w-1,-1,-1):
               new_arr[i][j] = image[i][w-1-j]
    return new_arr

def scale_image(image,scale_factor):
    h, w, cl = image.shape
    # scaling function
    # to round of hte scaled values I just used int() function which works similar to floor 
    nh, nw = int(h*scale_factor), int(w*scale_factor)
    new_arr = np.zeros((nh, nw, cl), dtype=np.uint8)
    # the new array will be of the required dimensions
    for i in range(0,nh):
        for j in range(0,nw):
            new_arr[i][j] = image[int(i/scale_factor)][int(j/scale_factor)]
    return new_arr

# output_file = '/op.jpeg'
# result_img = Image.fromarray(image)
# result_img.save(output_file)

cnt = 1
# counter to make a difference in the output
for inp in inps:
    # storing the input image path
    img_path = inp["image_path"]
    image = np.array(Image.open(img_path))
    op_path = f"/output{cnt}.jpeg"
    # making the 'op_path' a formatable string
    # and we use if-else conditional to check the operation to be performed 
    if inp['operation'] == 'translate':
        x_off = int(inp['params'][0])
        y_off = int(inp['params'][1])
        n_img = translate_image(image, x_off,y_off)
    elif inp["operation"] == "flip":
        axis = int(inp["params"][0])
        n_img = flip_image(image, axis)
    elif inp["operation"] == "scale":
        factor = float(inp["params"][0])
        n_img = scale_image(image,factor)
    op_img = Image.fromarray(n_img)
    op_img.save(op_path)
    cnt+=1
    
 # ------------ end -------------- #
