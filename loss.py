import pcl
import tensorflow as tf
import numpy as np


def loss(source):
    def homography_loss(y_true, y_pred):
        source_pcd = pcl.load(source)
        y_transformation_true = np.identity(3)
        a = y_pred - y_true
        return a
    return homography_loss
