import os
import numpy as np


batch_size = 14


def dat_loader(train_path):
    while True:
        archive = np.load(train_path)
        img = archive['images']
        truth = archive['truth']
        del archive
        # print(img[0])
        num_batches = len(truth)//batch_size
        i1 = np.array_split(img[0], num_batches)
        i2 = np.array_split(img[1], num_batches)
        truth = np.array_split(truth, num_batches)
        while truth:
            batch_i1 = i1.pop()
            batch_i2 = i2.pop()
            batch_truth = truth.pop()
            yield [batch_i1, batch_i2], batch_truth
