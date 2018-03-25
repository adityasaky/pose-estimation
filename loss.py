from keras import backend as k


def homography_loss(y_true, y_pred):
    a = y_pred - y_true
    return a
