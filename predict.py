from keras.models import load_model
import numpy as np
import os


def predict(batch_size, steps):
    test_images = list()
    model_path = './results/2018-04-11-...'
    image_path = ''
    model = load_model(model_path)
    for npz_file in os.listdir(image_path):
        f = np.load(image_path + npz_file)
        for i in range(len(f['images'])):
            test_images.append(f['images'][i])

    test_images = np.array(test_images)
    prediction = model.predict([test_images], batch_size=batch_size, verbose=0, steps=steps)
    return prediction


print(predict())