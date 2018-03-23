import os
import pickle
import numpy as np
import pcl
import sys


source_directory = "../pointclouds/"
training_directory = "../dataset/"
transformations_directory = "./pickle_files/"


height = 160
width = 160
height_meters = 80
width_meters = 60
all_transformations = dict()


def get_transformations():
    global all_transformations
    global transformations_directory
    for pkl_file in os.listdir(transformations_directory):
         with open(transformations_directory + pkl_file, "r") as t:
             transformation = pickle.load(t)
             all_transformations[pkl_file.split('.')[0]] = transformation


def scale_x(x):
    global width, width_meters
    return int(width * (width_meters * 0.5 + x) / width_meters)


def scale_y(y):
    global height, height_meters
    return height - 1 - int(height * (height_meters * 0.5 + y) / height_meters)


def map_to_image(x, y, z):
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
    z = pcd_array[:, 2]
    image = map_to_image(x, y, z)
    return image


def generate():
    global all_transformations
    global source_directory
    for pcd_file in os.listdir(source_directory):
        if not pcd_file.endswith('.pcd'):
            continue
        source_name = pcd_file.split('.')[0]
        print "Reading " + source_name + "..."
        all_points = pcl.load(source_directory + pcd_file)
        all_points_array = all_points.to_array()
        source_transformations_correspondence = dict()
        source_transformations_correspondence['images'] = dict()
        source_transformations_correspondence['truth_values'] = dict()
        source_transformations_correspondence['images']['i1'] = create_image(all_points_array)
        all_points_matrix = np.matrix.transpose(np.matrix(all_points_array))
        all_transformation_results = list()
        for transformation_key in all_transformations:
            print "Applying " + transformation_key + "..."
            transformation = all_transformations[transformation_key]
            transformation_result_matrix = np.dot(transformation, all_points_matrix)
            transformation_result_array = np.array(np.matrix.transpose(transformation_result_matrix))
            transformation_result_image = create_image(transformation_result_array)
            all_transformation_results.append(transformation_result_image)
            source_transformations_correspondence['truth_values'][transformation_key] = transformation.flatten()
        source_transformations_correspondence['images']['i2'] = all_transformation_results
        np.savez_compressed(training_directory + source_name, source_transformations_correspondence)


generate()