from keras.models import load_model
import numpy as np
import os


def predict():
    model_path = "/home/saky/tmp/project_archive/results/results/model_25.h5"
    file_path = "/home/saky/tmp/test_npz/file.npz"
    model = load_model(model_path)
    archive = np.load(file_path)
    test_images = archive['images']
    prediction = model.predict([test_images])
    print(prediction)
    print(archive['truth'])


predict()
