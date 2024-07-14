FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


CMD ["gunicorn","-k","geventwebsocket.gunicorn.workers.GeventWebSocketWorker"," -b","0.0.0.0:5000","-w","1","run:app"]  

# CMD ["python3", "run.py"]

# CMD ["waitress-serve", "--port=5000", "run:app"]