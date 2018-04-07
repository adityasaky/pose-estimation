import os
import numpy as np


def dat_loader(path, batch_size):
    while True:
        for dir, subdir, files in os.walk(path):
            for file in files:
                file_path = path + file
                archive = np.load(file_path)
                img = archive['images']
                truth = archive['truth']
                del archive
                num_batches = len(truth)//batch_size
                img = np.array_split(img, num_batches)
                truth = np.array_split(truth, num_batches)
                while truth:
                    batch_img = img.pop()
                    batch_truth = truth.pop()
                    yield batch_img, batch_truth
