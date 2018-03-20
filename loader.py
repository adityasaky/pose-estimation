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
                img = archive['images']
                truth = archive['truth']
                del archive
                # batch_i1 = img[0]
                # batch_i2 = img[1]
                # batch_truth = truth
                num_batches = len(truth)//batch_size
                i1 = np.array_split(img[0], num_batches)
                i2 = np.array_split(img[1], num_batches)
                truth = np.array_split(truth, num_batches)
                while truth:
                    batch_i1 = i1.pop()
                    batch_i2 = i2.pop()
                    batch_truth = truth.pop()
                    yield [batch_i1, batch_i2], batch_truth
