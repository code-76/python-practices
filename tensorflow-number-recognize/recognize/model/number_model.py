
from datasets.number_datasets import NumberDatasets
from PIL import Image
import tensorflow as tf

class NumberModel:
    
    def __init__(self):
        self.datasets = NumberDatasets()
        self.datasets.scale()
        self.x_train = self.datasets.x_train
        self.y_train = self.datasets.y_train
        self.x_test = self.datasets.x_test
        self.y_test = self.datasets.y_test

    def create_model(self, epochs=3):
        model  = tf.keras.models.Sequential()
        # input layer
        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        # hidden layer
        model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
        # output layer
        model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

        # settting the model compile to training
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, model, epochs=3):
        model.fit(self.x_train, self.y_train, epochs=epochs)
        # model.fit(
        #     self.x_train, 
        #     self.y_train, 
        #     batch_size=32, 
        #     validation_data=(self.x_test, self.y_test), 
        #     epochs=epochs, 
        #     validation_freq=1)

    def save(self, model, path="recognize", name="epic_num_reader.model"):
        model.save(path + "/" + name)

    def load_model(self, path="recognize", name="epic_num_reader.model"):
        model = tf.keras.models.load_model(path + "/" + name)
        return model

    def test(self, model=None):
        model = self.load_model() if model is None else model
        val_loss, val_acc = model.evaluate(self.x_test, self.y_test)
    
    def sample(self, index=0):
        return self.x_test[index]