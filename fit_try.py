from posenet.model import create_model
from keras.callbacks import History
from keras.optimizers import RMSprop, Adadelta
import keras.backend as K
from tensorflow.python import debug as tf_debug
from loss import loss_test
import numpy as np
import os


def main():
    '''sess = K.get_session()
    sess = tf_debug.LocalCLIDebugWrapperSession(sess)
    K.set_session(sess)'''
    model = create_model()
    history = History()
    
    base_lr = 0.005

    x_train = list()
    y_train = list()
    x_eval = list()
    y_eval = list()

    for npz_file in os.listdir('dataset_train/rot_only/'):
        f = np.load('dataset_train/rot_only/' + npz_file)
        for i in range(len(f['images'])):
            print(npz_file)
            print(i)
            x_train.append(f['images'][i])
            y_train.append(f['truth'][i])

    '''for npz_file in os.listdir('dataset_eval/all_transformations/'):
        f = np.load('dataset_eval/all_transformations/' + npz_file)
        for i in range(len(f['images'])):
            print(npz_file)
            print(i)
            x_eval.append(f['images'][i])
            y_eval.append(f['truth'][i])'''

    print(len(x_train))
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_eval = np.array(x_eval)
    y_eval = np.array(y_eval)

    rms = RMSprop(lr=base_lr, rho=0.9, epsilon=None, decay=0.0)
    ada = Adadelta(lr=base_lr, rho=0.95, epsilon=None, decay=0.0)
    print("Calling compile")
    #model.compile(optimizer=rms, loss=loss(sample_file),  metrics=['acc'])
    model.compile(optimizer=ada, loss='mean_squared_error',  metrics=['acc'])
    print("Compile done")

    for layer in model.layers:
        print("Input shape: " + str(layer.input_shape) + ". Output shape: " + str(layer.output_shape))

    print("Calling fit")
    model.fit([x_train],
              [y_train],
              batch_size=16,
              epochs=2,
              validation_split=0.1,
              #validation_data=([x_eval], [y_eval]),
              validation_data=None,
              shuffle=False,
              callbacks=[history])

#    predicted = model.predict([x_eval],
#                  batch_size=22)

#    print(history.History)

if __name__ == main():
    main()
