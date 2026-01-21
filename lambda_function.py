import tensorflow.lite as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('xception', target_size=(299, 299))
interpreter = tflite.Interpreter(model_path='xception_v4_1_08_0.940.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_index = input_details[0]['index']
output_index = output_details[0]['index']


# path = r"D:/GitHub/Garbage_Classification/dataset/test/battery/battery_4.jpg"


def predict(path):
    x = preprocessor.from_path(path)

    interpreter.set_tensor(input_index, x)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    return dict(zip(classes, preds[0]))


def lambda_handler(event, contet):
    url= event['url']

    result= predict (url)
    return result



