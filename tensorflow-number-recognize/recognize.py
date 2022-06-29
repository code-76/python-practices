import cv2
from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf

def create_model():
    # load datasets from keras samples
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # standardize the data
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    # build the model
    model  = tf.keras.models.Sequential()

    # input layer
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

    # hidden layer
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

    # output layer
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

    # configure the compliler to use the ADAM optimizer
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # start training
    model.fit(x_train, y_train, epochs=3)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(val_loss, val_acc)

    model.save('simple_model.h5')

def load_model():
    model = tf.keras.models.load_model('simple_model.h5')
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

# create_model()
predict('5.png')