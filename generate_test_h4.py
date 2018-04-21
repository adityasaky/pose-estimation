import pcl
import os
import cv2
import numpy as np


x_limit = 32.0
y_limit = 32.0
z_limit = -1.0
source_directory = "./filtered_new_set/"
target_directory = "./test_set/"
height = 64
width = 64

height_meters = 32
width_meters = 32

current = 10


def scale_x(x):
    global width_meters, width
    xs = int(width * (width_meters * 0.5 + x) / width_meters)
    return xs


def scale_y(y):
    global height_meters, height
    ys = int(height * (height_meters * 0.5 + y) / height_meters)
    return height - 1 - ys


def map_to_image(x, y):
    global height, width
    global height_meters, width_meters
    image = np.zeros((height, width, 3), np.uint8)
    for i in range(len(x)):
        if (abs(x[i]) <= width_meters * 0.5) & (abs(y[i]) <= height_meters * 0.5):
            xs = scale_x(x[i])
            ys = scale_y(y[i])
            image[ys, xs, 0] = 255
            image[ys, xs, 1] = 255
            image[ys, xs, 2] = 255
    return image


def create_image(pcd_array):
    x = pcd_array[:, 0]
    y = pcd_array[:, 1]
    return map_to_image(x, y)


def generate():
    while current <= 4310:
        current_file = str(current) + ".pcd"
        next_file = str(current + 10) + ".pcd"
        i1_points = pcl.load(current_file)
        i2_points = pcl.load(next_file)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        i1_points_array = i1_points.to_array()
        i2_points_array = i2_points.to_array()
        i1 = cv2.cvtColor(create_image(i1_points_array), cv2.COLOR_RGB2GRAY)
        i2 = cv2.cvtColor(create_image(i2_points_array), cv2.COLOR_RGB2GRAY)
        result_image = np.dstack((i1, i2))
        target_file_name = str(current) + "_" + str(current + 10)
        print("pairing" + current_file + "&" + next_file + "...")
        np.save(target_file_name, result_image)
