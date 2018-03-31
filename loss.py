import pcl
import tensorflow as tf
import numpy as np


def loss(source):
    def homography_loss(y_true, y_pred):
        print("HELLO")
        print(y_true.shape)
        source_pcd = pcl.load(source)
        a = y_pred - y_true
        return a
    return homography_loss
