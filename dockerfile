FROM --platform=linux/amd64 python:3.10-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

# CMD ["python3", "run.py"]

CMD ["waitress-serve", "--port=5000", "run:app"]