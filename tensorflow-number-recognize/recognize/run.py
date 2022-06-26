from model.number_model import NumberModel
from number_recognize import NumberRecognize

def gen_model(model: NumberModel):
    model = number_model.create_model()
    number_model.train(model=model, epochs=10)
    number_model.test(model=model)
    number_model.save(model=model)

def demo(model: NumberModel):
    recognize = NumberRecognize(model=model)
    recognize.demo()

def recognize(model: NumberModel, path: str, file: str):
    recognize = NumberRecognize(model=model)
    result = recognize.result(path="recognize/sample", file="number_6.jpg")
    print(result)

if __name__ == "__main__":
    number_model = NumberModel()
    # gen_model(model=number_model)
    demo(model=number_model)
    # recognize(model=number_model, path="recognize/sample", file="number_6.jpg")
    