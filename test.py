from posenet.model import create_model
from keras.optimizers import SGD
import os
import numpy as np
from loader import dat_loader


train_path = 'dataset/train/'
test_path = 'dataset/validation/'


def main():
    model = create_model()

    base_lr = 0.005

    sgd = SGD(lr=base_lr, momentum=0.9)
    model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])

    # model.summary()

    loader = dat_loader(train_path)
    #val_loader = dat_loader(test_path)

    model.fit_generator(loader,
                        epochs=3,
                        validation_data=val_loader,
                        validation_steps=9,
                        steps_per_epoch=9,
                        verbose=1,
                        shuffle=True)


if __name__ == main():
    main()
