FROM public.ecr.aws/lambda/python:3.8

RUN pip install -r requirements.txt
RUN pip install keras-image-helper
RUN pip install --etra-index-url \ 
https://google-coral.github.io/py-repo/ tflite_runtime
COPY xception_v4_1_08_0.940.tflite .
COPY lambda_function.py .
CMD ["lambda_function.lambda_handler"]



FROM python:3.8-slim

RUN pip install --upgrade pip

RUN pip install keras-image-helper

RUN pip install --extra-index-url \
    https://google-coral.github.io/py-repo/ tflite_runtime


