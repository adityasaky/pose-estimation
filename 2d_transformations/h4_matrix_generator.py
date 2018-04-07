import numpy as np
import pickle
import os


pickle_directory = "./pickle_files/"
h4_pickles_directory = "./h4_pickle_files/"
all_transformations = dict()

def get_transformations():
    global all_transformations
    global pickle_directory
    for pkl_file in os.listdir(pickle_directory):
        with open(pickle_directory + pkl_file, "rb") as t:
            transformation = pickle.load(t)
            all_transformations[pkl_file.split('.')[0]] = transformation


get_transformations()
p1 = np.array((0, 0, 1))
p2 = np.array((0, 128, 1))
p3 = np.array((128, 128, 1))
p4 = np.array((128, 0, 1))
for transformation_label in all_transformations:
    p1_prime = np.dot(all_transformations[transformation_label], p1)
    p2_prime = np.dot(all_transformations[transformation_label], p2)
    p3_prime = np.dot(all_transformations[transformation_label], p3)
    p4_prime = np.dot(all_transformations[transformation_label], p4)
    delta_p1 = p1 - p1_prime
    delta_p2 = p2 - p2_prime
    delta_p3 = p3 - p3_prime
    delta_p4 = p4 - p4_prime
    h4_matrix = np.zeros((4, 2))
    h4_matrix[0, 0] = delta_p1[0]
    h4_matrix[0, 1] = delta_p1[1]
    h4_matrix[1, 0] = delta_p2[0]
    h4_matrix[1, 1] = delta_p2[1]
    h4_matrix[2, 0] = delta_p3[0]
    h4_matrix[2, 1] = delta_p3[1]
    h4_matrix[3, 0] = delta_p4[0]
    h4_matrix[3, 1] = delta_p4[1]
    print("Saving " + transformation_label + "...")
    with open(h4_pickles_directory + transformation_label + ".pkl", "wb+") as f:
        pickle.dump(h4_matrix, f)
