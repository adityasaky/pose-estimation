import pcl
import os
import numpy as np


source_directory = "../pointclouds/"
target_directory = "../pointclouds_h4_test_32/"
for pcd_file in os.listdir(source_directory):
    pcd = pcl.load(source_directory + pcd_file)
    pcd_array = pcd.to_array()
    filtered_points_array = list()
    for point in pcd_array:
        if abs(point[0]) <= 32.0 and abs(point[1]) <= 32.0:
            point[0] += 32.0
            point[1] += 32.0
            filtered_points_array.append(point)
    target_pcd = pcl.PointCloud()
    target_pcd.from_array(np.array(filtered_points_array))
    target_pcd.to_file(target_directory + pcd_file)
