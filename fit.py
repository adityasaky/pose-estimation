from posenet.model import create_model
from keras.optimizers import RMSprop
from loss import homography_loss
import numpy as np


sample_path = 'dataset/canonical/1000.npz'


def main():
    model = create_model()

    base_lr = 0.005

    rms = RMSprop(lr=base_lr, rho=0.4, epsilon=None, decay=0.0)
    model.compile(optimizer=rms, loss=homography_loss,  metrics=['acc'])

    # model.summary()

    archive = np.load(sample_path)
    x = archive['images']
    y = archive['truth']

    model.fit(x=[x],
              y=[y],
              batch_size=None,
              epochs=5,
              verbose=2,
              validation_data=None,
              shuffle=False)


if __name__ == main():
    main()
