from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')


# development set up
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python3 run.py
# open 127.0.0.1:5000

# How to exit?
# deactivate

# About Docker running at local
# docker image build -t chi_vio .
# docker run -dp5000:5000 --name chi_vio_container chi_vio
# open 127.0.0.1:5000

