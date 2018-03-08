from posenet.model import create_model


def main():
    model = create_model()

    # Conf
    # batch_size = 64
    base_lr = 0.05

    sgd = SGD(lr=base_lr, momentum=0.9)
    model.compile(optimizer=sgd, loss='mean_squared_error', metrics=[accuracy])

    # train


if __name__ == '__main__':
    main()
