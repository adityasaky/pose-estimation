import pickle
import numpy as np


def computeHomographyFromH4P(H4p, img_dims):

    ps = np.array([[0,0],[0,img_dims[1]], [img_dims[0],img_dims[1]],[img_dims[0],0]])

    qs = ps + H4p



    P = np.zeros((9,9))

    for i in range(4):

        P[2*i]   = np.array([-ps[i,0], -ps[i,1], -1, 0, 0, 0, ps[i,0]*qs[i,0], ps[i,1]*qs[i,0], qs[i,0]])

        P[2*i+1] = np.array([0, 0, 0, -ps[i,0], -ps[i,1], -1, ps[i,0]*qs[i,1], ps[i,1]*qs[i,1], qs[i,1]])

    P[-1,-1] = 1



    b = np.zeros((9))

    b[-1] = 1



    H = np.linalg.solve(P,b)

    

    return H

source_3 = "./pickle_files_reduced/tm_2_4_3.pkl"
source_h4 = "./h4_pickle_files_reduced_64/tm_2_4_3.pkl"
f_3 = open(source_3, "r")
f_p_3 = pickle.load(f_3)
f_h4 = open(source_h4, "r")
f_p_h4 = pickle.load(f_h4)

print(f_p_3)
print(computeHomographyFromH4P(f_p_h4, [64, 64]).reshape((3,3)))
