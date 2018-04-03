import os
import sys
import pcl
import numpy as np
import pickle


x_limit = 64.0
y_limit = 64.0
z_limit = -1.0
source_directory = "../pointclouds/"
target_directory = "../pointclouds_h4/"
pickle_directory = "./pickle_files/"

height = 128
width = 128

height_meters = 64
width_meters = 64

all_transformations = dict()

def get_transformations():
    global all_transformations
    global pickle_directory
    for pkl_file in os.listdir(pickle_directory):
        with open(pickle_directory + pkl_file, "rb") as t:
            transformation = pickle.load(t, encoding='latin1')
            all_transformations[pkl_file.split('.')[0]] = transformation


def scalex(x):
    global width_meters, width
    xs = width * (width_meters * 0.5 + x) / width_meters
    return xs


def scaley(y):
    global height_meters, height
    ys = height * (height_meters * 0.5 + y) / height_meters
    return ys


get_transformations()

for pcd_file in os.listdir(source_directory):
    if not pcd_file.endswith('.pcd'):
        continue
    target = target_directory + pcd_file
    all_points = pcl.load(source_directory + pcd_file)
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    all_points_array = all_points.to_array()
    filtered_points_array = all_points_array[np.where((abs(all_points_array[:, 0]) < x_limit) & (abs(all_points_array[:, 1]) < y_limit) & (all_points_array[:, 2] >= z_limit))]
    for i in range(len(filtered_points_array)):
        filtered_points_array[i][0] = scalex(filtered_points_array[i][0])
        filtered_points_array[i][1] = scaley(filtered_points_array[i][1])
    filtered_points_matrix = np.matrix(filtered_points_array)
    #updated_points = pcl.PointCloud()
    #updated_points.from_array(filtered_points_array)
    #updated_points.to_file(target.encode('ASCII'))
    p1 = np.array((0, 0, 1))
    p2 = np.array((0, 128, 1))
    p3 = np.array((128, 128, 1))
    p4 = np.array((128, 0, 1))
    for transformation_label in all_transformations:
        p1_prime = np.dot(all_transformations[transformation_label], p1)
        p2_prime = np.dot(all_transformations[transformation_label], p2)
        p3_prime = np.dot(all_transformations[transformation_label], p3)
        p4_prime = np.dot(all_transformations[transformation_label], p4)
        print(p1 - p1_prime)
        print(p2 - p2_prime)
        print(p3 - p3_prime)
        print(p4 - p4_prime)
