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

    x_train = list()
    y_train = list()

    for npz_file in os.listdir('dataset_try/'):
        f = np.load('dataset_try/' + npz_file)
        for i in range(len(f['images'])):
            print(npz_file)
            print(i)
            x_train.append(f['images'][i])
            y_train.append(f['truth'][i])

    print(len(x_train))
    x_train = np.array(x_train)
    y_train = np.array(y_train)

    print("Calling fit")
    model.fit([x_train],
              [y_train],
              batch_size=16,
              epochs=2,
              verbose=2,
              validation_data=None,
              shuffle=False)

if __name__ == main():
    main()
