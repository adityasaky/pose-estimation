from keras.models import load_model
import numpy as np
import os 
import csv
import pickle


def computeHomographyFromH4P(H4p, img_dims):

    ps = np.array([[0,0],[0,img_dims[1]], [img_dims[0],img_dims[1]],[img_dims[0],0]])

    qs = ps - H4p



    P = np.zeros((9,9))

    for i in range(4):

        P[2*i]   = np.array([-ps[i,0], -ps[i,1], -1, 0, 0, 0, ps[i,0]*qs[i,0], ps[i,1]*qs[i,0], qs[i,0]])

        P[2*i+1] = np.array([0, 0, 0, -ps[i,0], -ps[i,1], -1, ps[i,0]*qs[i,1], ps[i,1]*qs[i,1], qs[i,1]])

    P[-1,-1] = 1



    b = np.zeros((9))

    b[-1] = 1



    H = np.linalg.solve(P,b)

    

    return H


def predict():
    all_pred_H = dict()
    model_path = "/home/saky/tmp/transpose100Epochs/model.h5"
    ground_truth_file = "./docs/ground_truth.txt"
    source_path = "/home/saky/tmp/test_data_pairs/"
    target_directory = "/home/saky/tmp/"
    target_file = "transpose"
    target_csv = target_directory + target_file + ".csv"
    csvfile = open(target_csv, "w")
    csvwriter = csv.writer(csvfile)
    target_pickle = target_directory + target_file + ".pkl"
    model = load_model(model_path)
    ground_truth = open(ground_truth_file, "r").readlines()
    for sample in os.listdir(source_path):
        sample_name = sample.split(".")[0]
        print("Predicting " + sample + "...")
        sample_1 = sample_name.split("_")[0]
        sample_2 = sample_name.split("_")[1]
        ground_truth_1 = ground_truth[int(sample_1)].split(" ")
        ground_truth_2 = ground_truth[int(sample_2)].split(" ")
        tx_t = float(ground_truth_2[0]) - float(ground_truth_1[0])
        ty_t = float(ground_truth_2[1]) - float(ground_truth_1[1])
        theta_t = float(ground_truth_2[2]) - float(ground_truth_1[2])
        file_path = source_path + sample
        archive = np.load(file_path)
        test_images = archive['images']
        prediction = model.predict([np.array([np.array(test_images)])])
        prediction = prediction.reshape((4, 2))
        prediction_H = computeHomographyFromH4P(prediction, [64, 64]).reshape((3, 3))
        sin = -prediction_H[0, 1]
        cos = prediction_H[0, 0]
        theta_p = np.arctan(sin / cos)
        A = np.zeros((2, 2))
        B = np.zeros((2, 1))
        A[0, 0] = prediction_H[0, 0]
        A[0, 1] = prediction_H[0, 1]
        A[1, 0] = prediction_H[1, 0]
        A[1, 1] = prediction_H[1, 1]
        B[0, 0] = prediction_H[0, 2]
        B[1, 0] = prediction_H[1, 2]
        C = np.linalg.solve(A, B)
        tx_p = C[0][0]
        ty_p = C[1][0]
        row = list()
        row.append(sample_name)
        row.append(tx_t)
        row.append(ty_t)
        row.append(theta_t)
        row.append(tx_p)
        row.append(ty_p)
        row.append(theta_p)
        csvwriter.writerow(row)
        all_pred_H[sample_name] = prediction_H
    with open(target_pickle, "wb") as pkl:
        pickle.dump(all_pred_H, pkl)


predict()

