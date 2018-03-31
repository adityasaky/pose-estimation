from posenet.model import create_model
from keras.optimizers import RMSprop
from loss import loss
import numpy as np
import os


sample_path = 'dataset_rot_only/canonical/3100.npz'
sample_file = 'pointclouds/3100.pcd'
sample_dir = 'dataset/canonical/'


def main():
    model = create_model()

    base_lr = 0.005

    rms = RMSprop(lr=base_lr, rho=0.4, epsilon=None, decay=0.0)
    print("Calling compile")
    model.compile(optimizer=rms, loss=loss(sample_file),  metrics=['acc'])
    print("Compile done")

    # model.summary()

    '''
    for in_file in os.listdir(sample_dir):
        archive = np.load(sample_dir + in_file)
        x = archive['images']
        y = archive['truth']
        model.fit(x=[x],
                  y=[y],
                  batch_size=None,
                  epochs=5,
                  verbose=2,
                  validation_data=None,
                  shuffle=False)
    '''
    archive = np.load(sample_path)
    x = archive['images']
    y = archive['truth']
    print("Calling fit")
    model.fit(x=[x],
              y=[y],
              batch_size=None,
              epochs=25,
              verbose=2,
              validation_data=None,
              shuffle=False)

if __name__ == main():
    main()
