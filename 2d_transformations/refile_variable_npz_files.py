import numpy as np
import os


source_directory = "../dataset_h4_full_test/"
target_directory = "../dataset_h4_full_test_refiled"
count_files = 39
count_samples = 4943


def generator():
    a = list()
    for npz_file in os.listdir(source_directory):
        archive = np.load(source_directory + npz_file)
        images = archive['images']
        truth = archive['truth']
        del archive
        size = len(truth)
        images =  np.array_split(images, size)
        truth =  np.array_split(truth, size)
        while truth:
            x = images.pop()
            y = truth.pop()
            yield x, y


def main():
    i1 = list()
    i2 = list()
    i = 0
    j = 0
    # print("creating iterable object")
    iter_obj = generator()
    while (j<count_files):
        while (i<count_samples):
            # print(i)
            sample = next(iter_obj)
            # print(len(sample[0]))
            # print(len(sample[1]))
            i1.append(sample[0])
            i2.append(sample[1])
            i += 1
        i1 = np.array(i1)
        i2 = np.array(i2)
        print(j)
        fname = target_directory + "file_" + str(j)
        np.savez_compressed(fname, images=i1, truth=i2)
        j += 1
    print("Done")


if __name__ == main():
    main()
 
