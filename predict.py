from keras.models import load_model
import numpy as np
import os


def predict():
    model_path = './results/2018-04-11-...'
    file_path = ''
    model = load_model(model_path)
    archive = np.load(file_path)
    test_files = archive['images']
    prediction = model.predict([test_images])
    print(prediction)


predict()
