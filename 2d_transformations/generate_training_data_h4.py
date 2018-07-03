import os
import cv2
import pcl
import numpy as np
import pickle
import sys


source_directory = "../pointclouds/"
target_directory = "/home/saky/tmp/original_set_center/"
h4_pickle_directory = "./h4_pickle_files_both_sides_center/"
pickle_directory = "./pickle_files_both_sides/"
height = 64
width = 64
all_transformations_h4 = dict()
all_transformations = dict()


def get_transformations():
    global all_transformations
    global all_transformations_h4
    global h4_pickle_directory
    global pickle_directory
    for pkl_file in os.listdir(pickle_directory):
        with open(pickle_directory + pkl_file, "rb") as t:
            transformation = pickle.load(t)
            all_transformations[pkl_file.split('.')[0]] = transformation
    for pkl_file in os.listdir(h4_pickle_directory):
        with open(h4_pickle_directory + pkl_file, "rb") as t:
            transformation = pickle.load(t)
            all_transformations_h4[pkl_file.split('.')[0]] = transformation


def make_pointcloud_positive(points_array):
    result = list()
    for point in points_array:
        if abs(point[0]) <= 32.0 and abs(point[1]) <= 32.0:
            point[0] += 32.0
            point[1] += 32.0
            result.append(point)
    return np.array(result)


def map_to_image(x, y):
    global height, width
    image = np.zeros((height, width, 3), np.uint8)
    for i in range(len(x)):
        xs = int(x[i])
        ys = height - 1 - int(y[i])
        image[ys, xs, 0] = 255
        image[ys, xs, 1] = 255
        image[ys, xs, 2] = 255
    return image


def create_image(pcd_array):
    x = pcd_array[:, 0]
    y = pcd_array[:, 1]
    return map_to_image(x, y)


def generate():
    get_transformations()
    for pcd_file in os.listdir(source_directory):
        if not pcd_file.endswith('.pcd'):
            continue
        source_name = pcd_file.split('.')[0]
        print("Reading " + source_name + "...")
        all_points = pcl.load(source_directory + pcd_file)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        all_points_array = all_points.to_array()
        source_positive = make_pointcloud_positive(all_points.to_array())
        len_source = len(all_points_array)
        source_image = cv2.cvtColor(create_image(source_positive), cv2.COLOR_RGB2GRAY)
        all_points_matrix = np.transpose(np.matrix(all_points_array))
        transformed_images = list()
        ground_truth = list()
        for transformation_label in all_transformations:
            print("Applying " + transformation_label + "...")
            transformation = all_transformations[transformation_label]
            transformation_result_matrix = np.transpose(np.dot(transformation, all_points_matrix))
            transformation_result_array = np.array(transformation_result_matrix)
            transformation_positive = make_pointcloud_positive(transformation_result_array)
            len_filtered = len(transformation_positive)
            if float(len_filtered) / float(len_source) < 0.6:
                continue
            transformation_result_image = cv2.cvtColor(create_image(transformation_positive), cv2.COLOR_RGB2GRAY)
            result_image = np.dstack((source_image, transformation_result_image))
            transformed_images.append(result_image)
            transformation_h4 = all_transformations_h4[transformation_label].flatten()
            ground_truth.append(transformation_h4)
            '''target_name = source_name + "_" + transformation_label.split('_')[1]
            print("Writing " + target_name + "...")
            np.savez_compressed(target_directory + target_name,
                                images=[result_image],
                                truth=[transformation_h4])'''
        print("Writing " + source_name + "...")
        np.savez_compressed(target_directory + source_name,
                        images=transformed_images,
                        truth=ground_truth)


generate()
