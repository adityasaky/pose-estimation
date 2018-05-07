from keras.models import load_model
import numpy as np
import os


def predict():
    model_path = "/home/saky/tmp/noTransposeModel/model.h5"
    file_path = "/home/saky/tmp/test_data_pairs/1000_1010.npz"
    model = load_model(model_path)
    archive = np.load(file_path)
    test_images = archive['images']
    prediction = model.predict([np.array([np.array(test_images)])])
    print(prediction)


predict()
