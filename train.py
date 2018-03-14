from posenet.model import create_model
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator


base_lr = 0.05
epochs = 1
epoch_step = 265
val_step = 239
val_batch_size = 16
img_ht = 160
img_wt = 160
train_dir_1 = 'dataset/train/train_1'
train_dir_2 = 'dataset/train/train_2'
test_dir_1 = 'dataset/validation/valid_1'
test_dir_2 = 'dataset/validation/valid_2'
batch_size = 64
input_imgen = ImageDataGenerator()
test_imgen = ImageDataGenerator()


def generate_generator_multiple(generator, dir1, batch_size, img_height, img_width):

    gen1 = generator.flow_from_directory(dir1,
                                          target_size=(img_height, img_width),
                                          batch_size=batch_size,
                                         shuffle=False)

    for i1_index in range(len(genX1)):
        # print(genX1.filenames[i1_index])
        filename1 = gen1.filenames[i1_index]
        target_directory = filename1.split('/')[1].split('.')[0]
        dir2 = './training_data/transformed_data/' + target_directory + '/'
        gen2 = generator.flow_from_directory(dir2,
                                              target_size=(img_height, img_width),
                                              batch_size=batch_size,
                                             shuffle=False)
        for i2_index in range(len(genX2)):
            filename2 = genX2.filenames[i2_index]
            yield ([gen1[i1_index], gen2[i2_index]], filename2)


def main():
    model = create_model()

    sgd = SGD(lr=base_lr, momentum=0.9)
    model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])

    input_generator = generate_generator_multiple(generator=input_imgen,
                                                  dir1=train_dir_1,
                                                  batch_size=batch_size,
                                                  img_height=img_ht,
                                                  img_width=img_wt)

    test_generator = generate_generator_multiple(test_imgen,
                                                 dir1=train_dir_1,
                                                 batch_size=val_batch_size,
                                                 img_height=img_ht,
                                                 img_width=img_wt)

    model.fit_generator(generator=input_generator, epochs=epochs,
                        validation_data=test_generator,
                        verbose=2,
                        steps_per_epoch=epoch_step,
                        validation_steps=val_step,
                        shuffle=True)


if __name__ == main():
    main()
