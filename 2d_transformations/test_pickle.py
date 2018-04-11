import numpy as np
import pickle


data = np.matrix('1 2 1')

with open('h4_pickle_files/tm_60_10_10.pkl', 'r') as f:
    transformation = pickle.load(f)
    print("Transformation is:")
    print(transformation)

with open('pickle_files/tm_60_10_10.pkl', 'r') as f:
    transformation = pickle.load(f)
    print("Transformation is:")
    print(transformation)
