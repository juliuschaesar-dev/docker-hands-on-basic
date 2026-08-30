FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["python3", "app.py"]
