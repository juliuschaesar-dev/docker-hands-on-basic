import os
from flask import Flask

app = Flask(__name__)

# Get the value of the CUSTOM_NAME argument from the environment variable
custom_name = os.getenv('CUSTOM_NAME', 'dibimbing-docker-app')


@app.route('/')
def hello_world():
    return f'Hello, {custom_name}!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
