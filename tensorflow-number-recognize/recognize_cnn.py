import csv
from filecmp import cmp
from operator import mod
from statistics import mode
from turtle import color
import cv2
from cv2 import add
import numpy as np
import matplotlib.pyplot as plt
from tensorboard import summary
import tensorflow as tf


def create_cnn_model():
    # https://www.youtube.com/watch?v=u3FLVbNn9Os
    # https://www.youtube.com/watch?v=L2cAjgc1-bo
    # load datasets from keras samples
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # standardize the data
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    # build the model
    model  = tf.keras.models.Sequential()

    # Fist CNN layer
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

    # Second CNN layer
    model.add(tf.keras.layers.Conv2D(64, (3, 3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

    # Third CNN layer
    model.add(tf.keras.layers.Conv2D(64, (3, 3)))
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

    # fully connect layer #1
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64))
    model.add(tf.keras.layers.Activation('softmax'))

    # fully connect layer #2
    model.add(tf.keras.layers.Dense(10))
    model.add(tf.keras.layers.Activation('softmax'))
    
    model.summary()

    # configure the compliler to use the ADAM optimizer
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # start training
    model.fit(x_train, y_train, epochs=3)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(val_loss, val_acc)

    model.save('cnn_model.h5')

def load_model():
    model = tf.keras.models.load_model('cnn_model.h5')
    return model

def predict(number_card):
    model = load_model()
    # [28, 28, 3]
    img = cv2.imread(f'sample/{number_card}')
    # [28, 28]
    img = img[:,:,0]
    img = np.invert(np.array([img]))
    # print(img.shape)
    prediction = model.predict(img)
    print(f'Number is {np.argmax(prediction)}')
    plt.imshow(img[0])
    plt.show()

# create_cnn_model()
predict('5.png')