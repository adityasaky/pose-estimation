import pcl
import numpy as np
import cv2
import os


source_directory = "../pointclouds_h4_test_32/"
target_directory = "../pointclouds_h4_test_32_images/"
width = 64
height = 64
for pcd_file in os.listdir(source_directory):
    source_name = pcd_file.split('.')[0]
    image = np.zeros((width, height, 3), np.uint8)
    pcd = pcl.load(source_directory + pcd_file)
    pcd_array = pcd.to_array()
    x = pcd_array[:, 0]
    y = pcd_array[:, 1]
    for i in range(len(x)):
        xs = int(x[i])
        ys = height - 1 - int(y[i])
        image[ys, xs, 0] = 255
        image[ys, xs, 1] = 255
        image[ys, xs, 2] = 255
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(target_directory + source_name + ".jpg", image)
