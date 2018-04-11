import sys
import pickle
import numpy as np
import os


pickle_diretory = "./h4_pickle_files/"
input_pickle = np.array((-6.51281883, -7.84749583, 74.04019122, 20.6778211, 102.56550816, -59.87518895, 22.0124981, -88.40050589))

for pickle_file in os.listdir(pickle_diretory):
    with open(pickle_diretory + pickle_file, "r") as f:
        p = pickle.load(f)
        p = np.array(p.flatten())
        if int(p[0]) == int(input_pickle[0]):
            if int(p[1]) == int(input_pickle[1]):
                print(p)
                print(pickle_file)
