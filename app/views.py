from app import app
from app import searchrequest
from flask import render_template, redirect
from flask import request
import json

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
    rating = []
    is_open = []
    deal = []
    length = requests.values()[2]
    for item in length:
        name.append(item['name']),
        link.append(item['url']),
        is_open.append(item['is_closed'])
        rating.append(item['rating'])
    print "------------------------------"
    print json.dumps(requests.values()[2], indent=4)
    return render_template('search.html', term = term, location = location, name = name, link =
            link, rating = rating, length = length, is_open = is_open)
