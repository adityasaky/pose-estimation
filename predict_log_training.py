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
    model_path = "/home/saky/tmp/both_sides_rot_only/transpose/model.h5"
    source_path = "/home/saky/tmp/project_export/dataset_both_sides_transpose_2/"
    target_directory = "/home/saky/tmp/"
    target_file = "two_sides_rot_only_transpose_training"
    target_csv = target_directory + target_file + ".csv"
    csvfile = open(target_csv, "w")
    csvwriter = csv.writer(csvfile)
    target_pickle = target_directory + target_file + ".pkl"
    model = load_model(model_path)
    for npz_file in os.listdir(source_path):
        source_name = npz_file.split(".")[0]
        archive = np.load(source_path + npz_file)
        img = archive['images']
        truth = archive['truth']
        for i in range(len(truth)):
            row = list()
            sample = img[i]
            label = source_name + "_" + str(i)
            print("Predicting " + label + "...")
            ground_truth = np.reshape(truth[i], (4, 2))
            ground_truth_H = np.reshape(computeHomographyFromH4P(ground_truth, [64, 64]), (3, 3))
            prediction = np.reshape(model.predict([np.array([np.array(sample)])]), (4, 2))
            prediction_H = np.reshape(computeHomographyFromH4P(prediction, [64, 64]), (3, 3))
            sin_t = -ground_truth_H[0, 1]
            cos_t = ground_truth_H[0, 0]
            theta_t = np.arctan(sin_t / cos_t)
            tx_t= 0
            ty_t = 0
            sin_p = -prediction_H[0, 1]
            cos_p = prediction_H[0, 0]
            theta_p = np.arctan(sin_p / cos_p)
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
            row.append(label)
            row.append(tx_t)
            row.append(ty_t)
            row.append(theta_t)
            row.append(tx_p)
            row.append(ty_p)
            row.append(theta_p)
            csvwriter.writerow(row)
            all_pred_H[label] = prediction_H
    with open(target_pickle, "wb") as pkl:
        pickle.dump(all_pred_H, pkl)


predict()

