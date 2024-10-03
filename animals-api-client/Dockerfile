# Use an official Python runtime as a parent image
#FROM python:3.11-slim
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

COPY . /app/
# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt


CMD python3 /app/src/main.py
#CMD sleep infinity