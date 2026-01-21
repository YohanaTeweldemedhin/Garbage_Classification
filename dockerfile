# AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Set working directory (Lambda uses /var/task)
WORKDIR /var/task

# Install system dependencies needed for TensorFlow Lite + image processing
RUN yum install -y \
    mesa-libGL \
    glib2 \
    libSM \
    libXext \
    libXrender \
    && yum clean all

# Copy requirements and install Python dependencies into Lambda task root
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt --target .

# Copy your Lambda function and model
COPY lambda_function.py .
COPY xception_v4_1_08_0.940.tflite .

# Lambda handler: file.function_name
CMD ["lambda_function.lambda_handler"]
