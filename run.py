from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5000,host='0.0.0.0')



# How to exit venv?
# deactivate

# About Docker running at local
# docker image build -t chi_vio .
# docker run -dp5000:5000 --name chi_vio_container chi_vio
# Limit hardware edition:
# docker run -dp5000:5000 --name chi_vio_container --cpus=1 --memory=512m chi_vio
# open 127.0.0.1:5000

# Development mode
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python3 run.py
# open 127.0.0.1:5000


# Production mode
# Use -> waitress <- as a WSGI server, easy to use
# pip install waitress
# waitress-serve --port=5000 run:app
