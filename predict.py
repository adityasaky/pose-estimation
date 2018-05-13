from keras.models import load_model
import numpy as np
import os


def computeHomographyFromH4P(H4p, img_dims):
    ps = np.array([[0, 0], [0, img_dims[1]], [img_dims[0], img_dims[1]], [img_dims[0], 0]])
    qs = ps - H4p
    P = np.zeros((9, 9))
    for i in range(4):
        P[2 * i] = np.array([-ps[i, 0], -ps[i, 1], -1, 0, 0, 0, ps[i, 0] * qs[i, 0], ps[i,1 ] * qs[i, 0], qs[i, 0]])
        P[2 * i + 1] = np.array([0, 0, 0, -ps[i, 0], -ps[i, 1], -1, ps[i, 0] * qs[i, 1], ps[i, 1] * qs[i, 1], qs[i, 1]])
    P[-1, -1] = 1
    b = np.zeros((9))
    b[-1] = 1
    H = np.linalg.solve(P, b)
    return H


def predict():
    model_path = "/home/saky/tmp/transpose100Epochs/model.h5"
    file_path = "/home/saky/tmp/test_data_pairs/1000_1010.npz"
    model = load_model(model_path)
    archive = np.load(file_path)
    test_images = archive['images']
    prediction = model.predict([np.array([np.array(test_images)])])
    print(prediction)
    prediction = prediction.reshape((4, 2))
    print(computeHomographyFromH4P(prediction, [64, 64]).reshape((3, 3)))


predict()
