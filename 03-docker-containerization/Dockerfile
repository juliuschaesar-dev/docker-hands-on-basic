# Define the base image
FROM python:3.8

# Define the argument variable (optional)
ARG CUSTOM_NAME=docker-app

# Set the working directory in the container
WORKDIR /app

# Copy dependency list and install it first (better layer caching)
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the application files to the container
COPY . /app

# Set the port that will be forwarded by the container
EXPOSE 8080

# Set the default command to run the application when the container is started
CMD ["python3", "app.py"]
