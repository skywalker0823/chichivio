from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')



# How to exit venv?
# deactivate

# About Docker running at local
# docker image build -t chi_vio .
# docker run -dp5000:5000 --name chi_vio_container chi_vio
# open 127.0.0.1:5000

# Development mode
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python3 run.py
# open 127.0.0.1:5000


# ========================
# Production mode for uWSGI(uwsgi)(still configuring)
# pip install uwsgi
# pip freeze > requirements.txt
# (uwsgi --ini uwsgi.ini) for local test
# docker image build -t chi_vio Dockerfile.prod
# docker run -dp5000:5000 --name chi_vio_container chi_vio

