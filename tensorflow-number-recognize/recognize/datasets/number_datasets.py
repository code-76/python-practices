from datasets.datasets_interface import DatasetsInterface
import tensorflow as tf
import matplotlib.pyplot as plt

class NumberDatasets(DatasetsInterface):

    def __init__(self):
        self.mnist = tf.keras.datasets.mnist
        (self.x_train, self.y_train), (self.x_test, self.y_test) = self.mnist.load_data()

    def scale(self): 
        self.x_train = tf.keras.utils.normalize(self.x_train, axis=1)
        self.x_test = tf.keras.utils.normalize(self.x_test, axis=1)

    def graph(self, index=0):
        plt.imshow(self.x_train[index], cmap=plt.cm.binary)
        plt.show()

    def log(self): 
        print("x_train shape:", self.x_train.shape)
        print("y_train shape:", self.y_train.shape)
