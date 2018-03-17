from posenet.model import create_model
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np


training_path = 'training_data/'
test_path = 'test_data/'


def loader(path):
    for npz_file in os.listdir(path):
        file = path + npz_file
        print(file)
        archive = np.load(file)
        inp = archive['images']
        grd = archive['truth']
        del archive
        return inp, grd


def main():
    model = create_model()

    base_lr = 0.005

    sgd = SGD(lr=base_lr, momentum=0.9)
    model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])

    # model.summary()

    train_file = loader(training_path)
    valid_file = loader(test_path)
    x = train_file[0]
    y = np.array(train_file[1])
    x1 = np.array(x[0])
    x2 = np.array(x[1])
    generator = ([x1, x2], y)
    model.fit_generator(generator,
                        epochs=1,
                        validation_data=valid_file,
                        steps_per_epoch=337,
                        verbose=2,
                        shuffle=False,
                        validation_steps=67)


if __name__ == main():
    main()
