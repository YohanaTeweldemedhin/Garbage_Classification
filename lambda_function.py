
import tensorflow as tf
from keras_image_helper import create_preprocessor
import os


classes = ['battery', 'cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']  # Update as per your dataset
preprocessor = create_preprocessor('xception', target_size=(299, 299))

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path='xception_v4_1_08_0.940.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_index = input_details[0]['index']
output_index = output_details[0]['index']

def predict(path):
    """Predict class probabilities for an image"""
    x = preprocessor.from_path(path)
    interpreter.set_tensor(input_index, x)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    return dict(zip(classes, preds[0]))

def lambda_handler(event, context):
    """Simulate AWS Lambda handler"""
    url = event['url']
    result = predict(url)
    return result

if __name__ == "__main__":
    # For local testing
    test_path = "dataset/test/battery/battery_4.jpg"
    print(predict(test_path))
