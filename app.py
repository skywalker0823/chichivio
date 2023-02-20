# static website, flask app, personal website, huichi
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/', static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact_post():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return render_template('contact.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')

# development set up
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python3 app.py
# open 127.0.0.1:5000

# How to exit?
# deactivate

# About Docker running at local
# docker image build -t chi_vio .
# docker run -dp5000:5000 --name chi_vio_container chi_vio
# open 127.0.0.1:5000

