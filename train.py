from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras import optimizers
# Add Dropout layer?
# from keras.models import Model
bat_size = 64
# epoch =

# load vgg16 network without the top layer
base_model = VGG16(input_shape=(120, 160, 3), include_top=False)

# instantiate a new sequential layer
top_model = Sequential()
top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
# creating fully connected layers of size 128 and 9
top_model.add(Dense(128, activation='relu'))
top_model.add(Dense(9, activation='relu'))

# combining top layer and base model to create a model
model = Sequential()
for l in base_model.layers:
    model.add(l)

model.add(top_model)

rmsprop = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
#model.fit(x=None, y=None, batch_size=bat_size, epochs=epoch, verbose=1)
# print(model.summary())
