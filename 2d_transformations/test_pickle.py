import numpy as np
import pickle


data = np.matrix('1 ; 2 ; 1');

with open('pickle_files/tm_60_4.pkl', 'r') as f:
    transformation = pickle.load(f)
    print "Transformation is:"
    print transformation
    print "Result is:"
    print transformation.dot(data)

