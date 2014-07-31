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
    requests = searchrequest.search(term, location)
    name = []
    link = []
    is_open = []
    length = requests.values()[2]
    for item in length:
        name.append(item['name']),
        link.append(item['url']),
        is_open.append(item['is_closed'])
    return render_template('search.html', term = term, location = location, name = name, link = link, is_open = is_open, length = length)
