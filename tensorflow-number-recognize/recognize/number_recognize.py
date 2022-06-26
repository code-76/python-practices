from model.number_model import NumberModel
from PIL import Image
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class NumberRecognize:
    def __init__(self, model: NumberModel):
        self.number_model = model

    def _fit_image(self, path="", file="number_1.jpg"):
        image = tf.keras.utils.load_img(
            path=path + "/" + file, 
            color_mode="grayscale", 
            target_size=(28, 28)
        )

        # image = tf.keras.utils.img_to_array(image)
        # image = Image.open(path + "/" + file)
        # image = image.resize((28, 28))
        # L = black and white
        image_array = np.array(image.convert('L'))
        # image_shape = np.expand_dims(image_array, axis=1)
        # for row in range(28):
        #     for col in range(28):
        #         if image_array[row][col] < 75:
        #             image_array[row][col] = 255
        #         else:
        #             image_array[row][col] = 0
        # image_array = image_array / 255
        return image_array
        
    def result(self, path="", file="number_1.jpg"):
        model = self.number_model.load_model()
        image = self._fit_image(path, file)
        tf.ensure_shape(image, [28, 28])
        # image = tf.keras.utils.normalize(image, axis=1)
        # print(image)
        # print(image.size)
        # print(image.shape)
        # plt.imshow(image)
        # plt.show()
        image = tf.reshape(image, (1,28,28))
        predictions = model.predict(image)
        result = [np.argmax(i) for i in predictions]
        return result

    def demo(self):
        model = self.number_model.load_model()
        sample = self.number_model.sample(9)
        plt.imshow(sample)
        plt.show()
        demo = tf.reshape(sample, (1,28,28))
        predictions = model.predict(demo)
        result = np.argmax(predictions[0])
        print(result)