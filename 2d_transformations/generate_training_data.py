import os
import pickle
import numpy as np
import pcl
import sys


source_directory = "../pointclouds_filtered/20.0_20.0_0.1/"
training_directory = "../training_data/"
transformations_directory = "./pickle_files/"

x_limit = 20.0
y_limit = 20.0
z_limit = 0.1

for pcd_file in os.listdir(source_directory):
    source_name = pcd_file.split('.')[0]
    if not pcd_file.endswith('.pcd'):
        continue
    print "Reading " + source_name
    all_points = pcl.load(source_directory + pcd_file)
    all_points_array = all_points.to_array()
    target_directory = training_directory + source_name + '/'
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    print "Filtering points"
    filtered_points_array = all_points_array[np.where((abs(all_points_array[:, 0]) < x_limit) & (abs(all_points_array[:, 1]) < y_limit) & (all_points_array[:, 2] >= z_limit))]
    filtered_points_matrix = np.matrix(filtered_points_array)
    filtered_points_matrix = np.matrix.transpose(filtered_points_matrix)
    for pkl_file in os.listdir(transformations_directory):
        with open(transformations_directory + pkl_file, 'r') as t:
            transformation = pickle.load(t)
            transformation_name = pkl_file.split('.')[0]
            target_name = source_name + "-" + transformation_name + ".pcd"
            print "Performing " + transformation_name
            transformation_result_matrix = np.dot(transformation, filtered_points_matrix)
            transformation_result_array = np.array(np.matrix.transpose(transformation_result_matrix))
            transformation_result = pcl.PointCloud()
            transformation_result.from_array(np.float32(transformation_result_array))
            print "Writing " + target_name
            transformation_result.to_file(target_directory + target_name)
