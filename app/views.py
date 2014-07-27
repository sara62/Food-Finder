from app import app
from searchrequest import *
from flask import render_template, redirect
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    term = request.form['Search']
    location = request.form['Location']
    return redirect('/')
