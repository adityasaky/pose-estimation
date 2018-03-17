import pickle
import os
import numpy as np
from scipy.misc import imread


path = 'Final Year Project/project/2d_transformations/pickle_files/'
src_path = 'input_1/'
trans_path = 'input_2/'


def create_ground_truth():
    truth = list()
    for dir, subdir, filelist in os.walk(path):
        for file in sorted(filelist):
            with open(path + file, "r") as t:
                a = np.load(t, allow_pickle=True)
                a = [a.reshape(9)]
                truth.append(a)
    return np.vstack(truth)


def create_numpy_input(ground_truth):
    for dir1, subdir1, filelist1 in os.walk(src_path):
        for file in sorted(filelist1):
            inp2 = list()
            if not file.endswith('.jpg'):
                continue
            name = file
            file_name = "file_" + file.split('.')[0]
            file = src_path + file
            i1 = imread(file)
            # f_name = file.split('.')[0]
            f_path = trans_path + name.split('.')[0]
            print f_path
            for dir2, subdir2, filelist2 in os.walk(f_path):
                for files in sorted(filelist2):
                    if not files.endswith('.jpg'):
                        continue
                    in_path = f_path + "/" + files
                    i2 = imread(in_path)
                    i2 = [i2]
                    inp2.append(i2)
            i2 = np.vstack(inp2)
            inp1 = [i1]
            inp1 = [inp1 * 126]
            inp1 = np.vstack(inp1)
            inp = np.array([inp1, i2])
            np.savez_compressed(file_name, images=inp, truth=ground_truth)
        print 'generated {}'.format(file_name)


def main():
    ground_truth = create_ground_truth()
    create_numpy_input(ground_truth)


if __name__ == main():
    main()
