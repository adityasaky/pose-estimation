import pcl
from keras import backend as K
import numpy as np
import tensorflow as tf


def loss_test(y_true, y_pred):

    with open('temp', 'a') as f:
        f.write(str(K.abs(y_pred)))
    return y_pred - y_true


def loss(source):
    def homography_loss(y_true, y_pred):
        print("HELLO")
        print(y_true.shape)
        source_pcd = pcl.load(source)
        a = y_pred - y_true
        return a
    return homography_loss
