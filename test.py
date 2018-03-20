from posenet.model import create_model
from keras.optimizers import SGD
import os
import numpy as np
from loader import dat_loader


train_path = 'dataset/train/'
test_path = 'dataset/validation/'
batch_size = 64


def main():
    model = create_model()

    base_lr = 0.001

    sgd = SGD(lr=base_lr, momentum=0.9)
    model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])

    # model.summary()

    model.fit_generator(dat_loader(train_path, batch_size),
                        epochs=2,
                        validation_data=None,
                        use_multiprocessing = True,
                        steps_per_epoch=270,
                        verbose=1,
                        shuffle=True)


if __name__ == main():
    main()
