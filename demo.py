from keras.models import load_model
import os
import pickle
import numpy as np
import math
import pcl
import cv2


pcd_file = "/home/saky/tmp/test_data_extra_32/600.pcd"
pkl_file = "2d_transformations/pickle_files_both_sides/tm_9.pkl"
height = 64
width = 64


def computeHomographyFromH4P(H4p, img_dims):
    ps = np.array([[0,0],[0,img_dims[1]], [img_dims[0],img_dims[1]],[img_dims[0],0]])
    qs = ps - H4p
    P = np.zeros((9,9))
    for i in range(4):
        P[2*i] = np.array([-ps[i,0], -ps[i,1], -1, 0, 0, 0, ps[i,0]*qs[i,0], ps[i,1]*qs[i,0], qs[i,0]])
        P[2*i+1] = np.array([0, 0, 0, -ps[i,0], -ps[i,1], -1, ps[i,0]*qs[i,1], ps[i,1]*qs[i,1], qs[i,1]])
    P[-1, -1] = 1
    b = np.zeros((9))
    b[-1] = 1
    H = np.linalg.solve(P,b)
    return H


def predict():
    ground_truth_value = pk_file.split("/")[-1].split(".")[0].split("_")[1]
    model_path = "/home/saky/tmp/both_sides_2/2018-05-14-18-27-02/model.h5"
    file_path = "test_file.npy"
    model = load_model(model_path)
    images = np.load(file_path)
    prediction = model.predict([np.array([np.array(images)])])
    prediction = prediction.reshape((4, 2))
    print("H4 prediction:")
    print(prediction)
    matrix = computeHomographyFromH4P(prediction, [64, 64]).reshape((3, 3))
    radian = np.arctan(-matrix[0, 1] / matrix[0, 0])
    degrees = math.degrees(radian)
    accuracy = 1 - abs((float(degrees) - float(ground_truth_value)) / float(ground_truth_value))
    print("Predicted homography matrix:")
    print(matrix)
    print("Predicted radian = {}".format(radian))
    print("Predicted degrees = {}".format(degrees))
    print("Ground truth degrees = {}".format(ground_truth_value))
    print("Accuracy = {}".format(accuracy))


def map_to_image(x, y):
    global height, width
    image = np.zeros((height, width, 3), np.uint8)
    x_filtered = x[x < 64]
    y_filtered = y[y < 64]
    '''print(len(x))
    print(len(x_filtered))
    print(len(y))
    print(len(y_filtered))
    print(x_filtered[x_filtered < 0])
    print(y_filtered[y_filtered > 64])'''
    for i in range(len(x)):
        xs = int(x[i])
        ys = height - 1 - int(y[i])
        if xs >= 64:
            print(i)
        image[ys, xs, 0] = 255
        image[ys, xs, 1] = 255
        image[ys, xs, 2] = 255
    return image


def create_image(pcd_array):
    x = pcd_array[:, 0]
    y = pcd_array[:, 1]
    return map_to_image(x, y)


def generate():
    all_points = pcl.load(pcd_file)
    all_points_array = all_points.to_array()
    filtered_transformation_result_array = list()
    len_source = len(all_points_array)
    print("Creating image...")
    source_image = cv2.cvtColor(create_image(all_points_array), cv2.COLOR_RGB2GRAY)
    all_points_matrix = np.matrix.transpose(np.matrix(all_points_array))
    with open(pkl_file, "rb") as t:
        transformation = pickle.load(t)
    transformation_result_matrix = np.dot(transformation, all_points_matrix)
    transformation_result_array = np.array(np.matrix.transpose(transformation_result_matrix))
    for point in transformation_result_array:
        if 0.0 <= point[0] <= 64.0 and 0.0 <= point[1] <= 64.0:
            filtered_transformation_result_array.append(point)
    filtered_transformation_result_array = np.array(filtered_transformation_result_array)
    len_filtered = len(filtered_transformation_result_array)
    transformation_result_image = cv2.cvtColor(create_image(transformation_result_array), cv2.COLOR_RGB2GRAY)
    result_image = np.dstack((source_image, transformation_result_image))
    print("Sample generated...")
    np.save("test_file", result_image)
    predict()
    '''target_pcd = pcl.PointCloud()
    src_pcd = pcl.PointCloud()
    filtered_transformation_result_array[:, 2] = 0
    all_points_array[:, 2] = 0
    target_pcd.from_array(np.float32(filtered_transformation_result_array))
    src_pcd.from_array(np.float32(all_points_array))
    target_directory = "icp_test/" + "deg_7.5/"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    # print(target_directory + "trans_pcd.pcd")
    target_pcd.to_file(target_directory + "trans.pcd")
    src_pcd.to_file(target_directory + "src.pcd")'''


generate()
