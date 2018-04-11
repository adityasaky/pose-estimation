import keras
import numpy as np
import os

def predictor(batch_size, steps):
    test_images = list()
    
    for npz_file in os.listdir('dataset_test/h4/'):
        f = np.load('dataset_test/h4/' + npz_file)
	for i in range(len(f['images'])):
            test_images.append(f['images'][i])

    test_images = np.array(test_images)
    prediction = model.predict([test_images],batch_size = batch_size, verbose = 0, steps = steps)
