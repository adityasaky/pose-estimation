import numpy as np
import cv2
import pcl
import pickle


width_meters = 64
height_meters = 64
width = 128
height = 128


def scale_x(x):
    global width_meters, width
    xs = width * (width_meters * 0.5 + x) / width_meters
    return xs


def scale_y(y):
    global height_meters, height
    ys = height * (height_meters * 0.5 + y) / height_meters
    return ys


def move_to_positive(x, y, z):
    global height, width
    global height_meters, width_meters
    all_points = list()
    for i in range(len(x)):
        if (abs(x[i]) <= width_meters * 0.5) & (abs(y[i]) <= height_meters * 0.5):
            xs = scale_x(x[i])
            ys = scale_y(y[i])
            zs = z[i]
            point = np.array((xs, ys, zs))
            all_points.append(point)
    return np.array(all_points)


def scale_x_image(x):
    global width_meters, width
    xs = int(width * (width_meters * 0.5 + x) / width_meters)
    return xs


def scale_y_image(y):
    global height_meters, height
    ys = int(height * (height_meters * 0.5 + y) / height_meters)
    return height - 1 - ys


def map_to_image(x, y):
    global height, width
    global height_meters, width_meters
    image = np.zeros((height, width, 3), np.uint8)
    for i in range(len(x)):
        if (abs(x[i]) <= width_meters * 0.5) & (abs(y[i]) <= height_meters * 0.5):
            xs = scale_x_image(x[i])
            ys = scale_y_image(y[i])
            image[ys, xs, 0] = 255
            image[ys, xs, 1] = 255
            image[ys, xs, 2] = 255
    return image


def create_image(pcd_array):
    x = pcd_array[:, 0]
    y = pcd_array[:, 1]
    return map_to_image(x, y)


source_pointcloud_file = "/home/saky/tmp/test_data_extra/1265.pcd"
transformation_directory = "./pickle_files_half/"
transformation_pickle = "tm_3.0_2_4-.pkl"
h4_directory = "./h4_pickle_files_half/"
target = "/home/saky/tmp/test_npz/file.npz"
transformation = pickle.load(open(transformation_directory + transformation_pickle, "r"))
h4_transformation = pickle.load(open(h4_directory + transformation_pickle, "r"))
source_pointcloud = pcl.load(source_pointcloud_file)
source_pointcloud_array = source_pointcloud.to_array()
x = source_pointcloud_array[:, 0]
y = source_pointcloud_array[:, 1]
z = source_pointcloud_array[:, 2]
source_pointcloud_positive_array = move_to_positive(x, y, z)
source_image = cv2.cvtColor(create_image(source_pointcloud_array), cv2.COLOR_RGB2GRAY)
source_pointcloud_matrix = np.transpose(np.matrix(source_pointcloud_positive_array))
result_pointcloud_matrix = np.transpose(np.dot(transformation, source_pointcloud_matrix))
result_pointcloud_array = np.array(result_pointcloud_matrix)
filtered_points_array = list()
for point in result_pointcloud_array:
    if 0.0 <= point[0] <= 128.0 and 0.0 <= point[1] <= 128.0:
        filtered_points_array.append(point)
filtered_points_array = np.array(filtered_points_array)
transformation_result_image = cv2.cvtColor(create_image(filtered_points_array), cv2.COLOR_RGB2GRAY)
resultant_image = np.dstack((source_image, transformation_result_image))
ground_truth = h4_transformation.flatten()
np.savez_compressed(target,
                    images=[resultant_image],
                    truth=[ground_truth])