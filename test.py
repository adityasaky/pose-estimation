from posenet.model_h4 import create_model
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adadelta
from loader import dat_loader
import datetime
import os


def main():
    model = create_model()
    base_lr = 0.005
    epochs = 2
    batch_size = 8
    steps_per_epoch = 24715
    day = str(datetime.datetime.now()).split('.')[0].split(' ')[0]
    time = '-'.join(str(datetime.datetime.now()).split('.')[0].split(' ')[1].split(':'))
    timestamp = day + '-' + time
    result_path = "./results/" + timestamp + "/"
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    with open(result_path + "summary", "w+") as summary:
        summary.write("Time: " + timestamp + "\n")
        summary.write("No of epochs: " + str(epochs) + "\n")
        summary.write("No of samples: " + str(batch_size * steps_per_epoch) "\n")
        summary.write("Batch size: " + str(batch_size) + "\n")
        summary.write("Steps per epoch: " + str(steps_per_epoch) + "\n")
    ada = Adadelta(lr=base_lr, rho=0.95, epsilon=None, decay=0.0)
    print("Calling compile")
    model.compile(optimizer=ada, loss='mean_squared_error',  metrics=['acc'])
    print("Compile done")
    checkpoint_path = result_path + "model_checkpoint.h5"
    checkpointer = ModelCheckpoint(filepath=checkpoint_path, monitor='loss', save_weights_only=False, mode='auto')
    print("Calling fit")
    model.fit_generator(dat_loader('./dataset_h4_full_test_refiled/', batch_size),
                                    epochs=epochs,
                                    validation_data=None,
                                    steps_per_epoch=steps_per_epoch,
                                    callbacks=[checkpointer],
                                    shuffle=False)

    model.save(result_path + "model.h5")
    model.save_weights(result_path + "model_weights.h5")


if __name__ == main():
    main()
