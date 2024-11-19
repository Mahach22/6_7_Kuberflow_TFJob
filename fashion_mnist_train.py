# fashion_mnist_train.py
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist
import numpy as np


def load_and_preprocess_data():
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    return (x_train, y_train), (x_test, y_test)


def build_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def train_and_save_model():
    (x_train, y_train), (x_test, y_test) = load_and_preprocess_data()
    model = build_model()
    model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)
    model.evaluate(x_test, y_test, verbose=2)
    model.save("fashion_mnist_model.h5")
    print("Model saved to fashion_mnist_model.h5")


if __name__ == "__main__":
    train_and_save_model()
