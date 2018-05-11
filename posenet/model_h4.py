from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, InputLayer, Flatten


def create_model():
    model = Sequential()
    model.add(InputLayer((64, 64, 2), name='input_1'))

    model.add(Conv2D(64, 3, padding='same', activation='relu', name='conv_1'))
    model.add(Conv2D(64, 3, padding='same', activation='relu', name='conv_2'))

    model.add(MaxPooling2D(strides=(2, 2), name='max_pooling2d_1'))

    model.add(Conv2D(64, 3, padding='same', activation='relu', name='conv_3'))
    model.add(Conv2D(64, 3, padding='same', activation='relu', name='conv_4'))

    model.add(MaxPooling2D(strides=(2, 2), name='max_pooling2d_2'))

    model.add(Conv2D(128, 3, padding='same', activation='relu', name='conv_5'))
    model.add(Conv2D(128, 3, padding='same', activation='relu', name='conv_6'))

    model.add(MaxPooling2D(strides=(2, 2), name='max_pooling2d_3'))

    model.add(Conv2D(128, 3, padding='same', activation='relu', name='conv_7'))
    model.add(Conv2D(128, 3, padding='same', activation='relu', name='conv_8'))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu', name='dense_1'))
    model.add(Dense(8, activation='relu', name='dense_2'))

    return model
