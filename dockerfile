FROM --platform=linux/amd64 python:3.10.10-alpine3.17

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]