#!/usr/bin/python

from keras.layers import Input, Reshape, Conv2D, MaxPooling2D, Flatten, Dense
from keras.layers import concatenate
from keras.models import Model


def create_model():
    main_input = Input(shape=(20, 20, 128), name='main_input')

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv1')(main_input)
    x = MaxPooling2D(strides=(2, 2), name='pool1')(x)

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv2')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv3')(x)
    x = MaxPooling2D(strides=(2, 2), name='pool2')(x)

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv4')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv5')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv6')(x)
    x = MaxPooling2D(strides=(2, 2), name='pool3')(x)

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv7')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv8')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv9')(x)
    x = MaxPooling2D(strides=(2, 2), name='pool4')(x)

    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv10')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv11')(x)
    x = Conv2D(128, 3, padding='same', strides=(1, 1), activation='relu', name='conv12')(x)
    x = MaxPooling2D(strides=(2, 2), name='pool5')(x)

    x = Flatten()(x)
    x = Dense(128, activation='relu', name='fc')(x)
    main_output = Dense(9, activation='relu', name='main_output')(x)

    model = Model(inputs=[main_input], outputs=[main_output])
    print(model.summary())

    return model
