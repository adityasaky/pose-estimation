from posenet.model_h4 import create_model
from keras.callbacks import History
from keras.optimizers import RMSprop, Adadelta
import keras.backend as K
from loader import dat_loader
import numpy as np
import os


def main():
    
    model = create_model()
    
    base_lr = 0.005



    ada = Adadelta(lr=base_lr, rho=0.95, epsilon=None, decay=0.0)
    print("Calling compile")
    model.compile(optimizer=ada, loss='mean_squared_error',  metrics=['acc'])
    print("Compile done")

    print("Calling fit")
    model.fit_generator(dat_loader('dataset_train/h4/', 21),
                                    epochs=3,
                                    validation_data=None,
                                    steps_per_epoch=72,
                                    shuffle=False)

    model.save('/home/ajay/test/sample_trained_models/shi_tomasi/my_model.h5')
    model.save_weights('/home/ajay/sample_trained_models/shi_tomasi/my_model_weights.h5')


if __name__ == main():
    main()
