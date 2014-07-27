from app import app
from app import searchrequest
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
    test = searchrequest.search(term, location)
    return render_template('search.html', term = term, location = location, test = test)
