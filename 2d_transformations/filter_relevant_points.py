import os
import pcl
import numpy as np


x_limit = 20.0
y_limit = 20.0
z_limit = 0.1
source_directory = "../pointclouds/"
target_directory = "../pointclouds_filtered/" + str(x_limit) + "_" + str(y_limit) + "_" + str(z_limit) + "/"

for pcd_file in os.listdir(source_directory):
    all_points = pcl.load(source_directory + pcd_file)
    source_name = pcd_file.split('.')[0]
    print "Reading " + source_name + "..."
    target_name = source_name + "-" + str(x_limit) + "_" + str(y_limit) + "_" + str(z_limit) + ".pcd"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    all_points_array = all_points.to_array()
    filtered_points_array = all_points_array[np.where((abs(all_points_array[:, 0]) < x_limit) & (abs(all_points_array[:, 1]) < y_limit) & (all_points_array[:, 2] >= 0.1))]
    filtered_points = pcl.PointCloud()
    filtered_points.from_array(filtered_points_array)
    print "Writing " + target_name
    filtered_points.to_file(target_directory + target_name)
