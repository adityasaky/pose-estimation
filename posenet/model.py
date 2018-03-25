#!/usr/bin/python

from keras.layers import Input, Reshape, Conv2D, MaxPooling2D, Flatten, Dense
from keras.layers import concatenate
from keras.models import Model


def create_model():
    input_1 = Input(shape=(20, 20, 128), name='input_1')
    # reshape_1 = Reshape((20, 20, 64), name='reshape_1')(input_1)

    # input_2 = Input(shape=(160, 160), name='input_2')
    # reshape_2 = Reshape((20, 20, 64), name='reshape_2')(input_2)

    # x = concatenate([reshape_1, reshape_2])

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='block1_conv1')(input_1)
    x = MaxPooling2D(strides=(2, 2), name='block1_pool')(x)

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='block2_conv1')(x)
    x = MaxPooling2D(strides=(2, 2), name='block2_pool')(x)

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='block3_conv1')(x)

    x = Flatten()(x)
    x = Dense(128, activation='relu', name='fc1')(x)
    main_output = Dense(9, activation='relu', name='main_output')(x)

    model = Model(inputs=[input_1], outputs=[main_output])
    # print(model.summary())

    return model
