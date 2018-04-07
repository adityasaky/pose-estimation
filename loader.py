import os
import numpy as np


# batch_size = 14


def dat_loader(path, batch_size):
    while True:
        for dir, subdir, files in os.walk(path):
            for file in files:
                print(file)
                file_path = path + file
                archive = np.load(file_path)
                images = archive['images']
                truth = archive['truth']
                num_batches = len(truth)//batch_size
                image_batch = np.array_split(images, num_batches)
                truth_batch = np.array_split(truth, num_batches)
                while truth_batch:
                    single_image = image_batch.pop()
                    single_truth = truth_batch.pop()
                    yield [single_image], [single_truth]
