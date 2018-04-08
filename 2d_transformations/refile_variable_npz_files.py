import numpy as np
import os


source_directory = "../dataset_h4_full_test/"
target_directory = "../dataset_h4_full_test_refiled"
count_files = 39
count_samples = 4943


def generator():
    for npz_file in os.listdir(source_directory):
        archive = np.load(source_directory + npz_file)
        images = archive['images']
        truth = archive['truth']
        del archive
        batches = len(images)
        images = np.array_split(images, batches)
        truth = np.array_split(truth, batches)
        while truth:
            image = images.pop()
            truth_value = truth.pop()
            yield image, truth_value


def refile():
    g = generator()
    print(g)


refile()